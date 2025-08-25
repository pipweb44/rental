from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from properties.models import Property, PropertyRequest, RentalRequest, PropertyImage

@staff_member_required
def dashboard(request):
    """لوحة التحكم الرئيسية"""
    pending_property_requests = PropertyRequest.objects.filter(status='pending').count()
    pending_rental_requests = RentalRequest.objects.filter(status='pending').count()
    total_properties = Property.objects.filter(is_approved=True).count()

    context = {
        'pending_property_requests': pending_property_requests,
        'pending_rental_requests': pending_rental_requests,
        'total_properties': total_properties,
    }
    return render(request, 'admin_panel/dashboard.html', context)

@staff_member_required
def property_requests(request):
    """طلبات عرض العقارات"""
    requests = PropertyRequest.objects.all().order_by('-created_at')
    context = {
        'requests': requests,
    }
    return render(request, 'admin_panel/property_requests.html', context)

@staff_member_required
def rental_requests(request):
    """طلبات الإيجار"""
    requests = RentalRequest.objects.all().order_by('-created_at')
    context = {
        'requests': requests,
    }
    return render(request, 'admin_panel/rental_requests.html', context)

@staff_member_required
def approve_property_request(request, request_id):
    """قبول طلب عرض عقار"""
    property_request = get_object_or_404(PropertyRequest, id=request_id)

    if property_request.status == 'pending':
        property_request.status = 'approved'
        property_request.save()

        # إنشاء العقار
        property_obj = Property.objects.create(
            owner=property_request.owner,
            title=property_request.title,
            description=property_request.description,
            property_type=property_request.property_type,
            address=property_request.address,
            city=property_request.city,
            area=property_request.area,
            bedrooms=property_request.bedrooms,
            bathrooms=property_request.bathrooms,
            price=property_request.price,
            is_approved=True
        )

        # نسخ الصور
        for img in property_request.images.all():
            PropertyImage.objects.create(
                property=property_obj,
                image=img.image,
                is_main=img.is_main
            )

        messages.success(request, 'تم قبول طلب العقار وإنشاء العقار بنجاح!')

    return redirect('admin_panel:property_requests')

@staff_member_required
def reject_property_request(request, request_id):
    """رفض طلب عرض عقار"""
    property_request = get_object_or_404(PropertyRequest, id=request_id)

    if property_request.status == 'pending':
        property_request.status = 'rejected'
        property_request.save()
        messages.success(request, 'تم رفض طلب العقار!')

    return redirect('admin_panel:property_requests')

@staff_member_required
def approve_rental_request(request, request_id):
    """قبول طلب إيجار"""
    rental_request = get_object_or_404(RentalRequest, id=request_id)

    if rental_request.status == 'pending':
        rental_request.status = 'approved'
        rental_request.save()
        messages.success(request, 'تم قبول طلب الإيجار!')

    return redirect('admin_panel:rental_requests')

@staff_member_required
def reject_rental_request(request, request_id):
    """رفض طلب إيجار"""
    rental_request = get_object_or_404(RentalRequest, id=request_id)

    if rental_request.status == 'pending':
        rental_request.status = 'rejected'
        rental_request.save()
        messages.success(request, 'تم رفض طلب الإيجار!')

    return redirect('admin_panel:rental_requests')
