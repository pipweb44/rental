from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Property, PropertyRequest, RentalRequest
from .forms import PropertyRequestForm, RentalRequestForm

def home(request):
    """الصفحة الرئيسية"""
    featured_properties = Property.objects.filter(is_approved=True, status='available')[:6]
    context = {
        'featured_properties': featured_properties,
    }
    return render(request, 'properties/home.html', context)

def property_list(request):
    """قائمة العقارات"""
    properties = Property.objects.filter(is_approved=True, status='available')

    # فلترة حسب النوع
    property_type = request.GET.get('type')
    if property_type:
        properties = properties.filter(property_type=property_type)

    # فلترة حسب المدينة
    city = request.GET.get('city')
    if city:
        properties = properties.filter(city__icontains=city)

    # فلترة حسب السعر
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        properties = properties.filter(price__gte=min_price)
    if max_price:
        properties = properties.filter(price__lte=max_price)

    paginator = Paginator(properties, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'property_types': Property.PROPERTY_TYPES,
    }
    return render(request, 'properties/property_list.html', context)

def property_detail(request, pk):
    """تفاصيل العقار"""
    property_obj = get_object_or_404(Property, pk=pk, is_approved=True)
    context = {
        'property': property_obj,
    }
    return render(request, 'properties/property_detail.html', context)

@login_required
def rent_request(request, property_id):
    """طلب إيجار عقار"""
    property_obj = get_object_or_404(Property, pk=property_id, is_approved=True, status='available')

    if request.method == 'POST':
        form = RentalRequestForm(request.POST)
        if form.is_valid():
            rental_request = form.save(commit=False)
            rental_request.client = request.user
            rental_request.property = property_obj
            rental_request.save()
            messages.success(request, 'تم إرسال طلب الإيجار بنجاح!')
            return redirect('properties:my_requests')
    else:
        form = RentalRequestForm()

    context = {
        'form': form,
        'property': property_obj,
    }
    return render(request, 'properties/rent_request.html', context)

@login_required
def add_property_request(request):
    """طلب عرض عقار"""
    if request.method == 'POST':
        form = PropertyRequestForm(request.POST, request.FILES)
        if form.is_valid():
            property_request = form.save(commit=False)
            property_request.owner = request.user
            property_request.save()
            messages.success(request, 'تم إرسال طلب عرض العقار بنجاح!')
            return redirect('properties:my_requests')
    else:
        form = PropertyRequestForm()

    context = {
        'form': form,
    }
    return render(request, 'properties/add_property_request.html', context)

@login_required
def my_requests(request):
    """طلباتي"""
    if request.user.user_type == 'owner':
        property_requests = PropertyRequest.objects.filter(owner=request.user).order_by('-created_at')
        context = {
            'property_requests': property_requests,
        }
    else:  # client
        rental_requests = RentalRequest.objects.filter(client=request.user).order_by('-created_at')
        context = {
            'rental_requests': rental_requests,
        }

    return render(request, 'properties/my_requests.html', context)

@login_required
def my_properties(request):
    """عقاراتي"""
    properties = Property.objects.filter(owner=request.user).order_by('-created_at')
    context = {
        'properties': properties,
    }
    return render(request, 'properties/my_properties.html', context)
