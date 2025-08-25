from django.contrib import admin
from .models import Property, PropertyImage, PropertyRequest, PropertyRequestImage, RentalRequest

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'property_type', 'city', 'price', 'status', 'is_approved', 'created_at')
    list_filter = ('property_type', 'status', 'is_approved', 'city')
    search_fields = ('title', 'description', 'address', 'owner__username')
    inlines = [PropertyImageInline]

    def save_model(self, request, obj, form, change):
        if not change:  # إذا كان عقار جديد
            obj.owner = request.user
        super().save_model(request, obj, form, change)

class PropertyRequestImageInline(admin.TabularInline):
    model = PropertyRequestImage
    extra = 1

@admin.register(PropertyRequest)
class PropertyRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'property_type', 'city', 'price', 'status', 'created_at')
    list_filter = ('property_type', 'status', 'city')
    search_fields = ('title', 'description', 'address', 'owner__username')
    inlines = [PropertyRequestImageInline]

    def save_model(self, request, obj, form, change):
        # إذا تم قبول الطلب، إنشاء عقار جديد
        if obj.status == 'approved' and change:
            # التحقق من عدم وجود عقار مرتبط بهذا الطلب
            if not Property.objects.filter(title=obj.title, owner=obj.owner).exists():
                property_obj = Property.objects.create(
                    owner=obj.owner,
                    title=obj.title,
                    description=obj.description,
                    property_type=obj.property_type,
                    address=obj.address,
                    city=obj.city,
                    area=obj.area,
                    bedrooms=obj.bedrooms,
                    bathrooms=obj.bathrooms,
                    price=obj.price,
                    is_approved=True
                )
                # نسخ الصور
                for img in obj.images.all():
                    PropertyImage.objects.create(
                        property=property_obj,
                        image=img.image,
                        is_main=img.is_main
                    )
        super().save_model(request, obj, form, change)

@admin.register(RentalRequest)
class RentalRequestAdmin(admin.ModelAdmin):
    list_display = ('property', 'client', 'preferred_start_date', 'duration_months', 'status', 'created_at')
    list_filter = ('status', 'preferred_start_date')
    search_fields = ('property__title', 'client__username', 'message')
