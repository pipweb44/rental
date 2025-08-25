from django.db import models
from django.conf import settings

class Property(models.Model):
    PROPERTY_TYPES = (
        ('apartment', 'شقة'),
        ('villa', 'فيلا'),
        ('office', 'مكتب'),
        ('shop', 'محل تجاري'),
        ('warehouse', 'مستودع'),
    )

    STATUS_CHOICES = (
        ('available', 'متاح'),
        ('rented', 'مؤجر'),
        ('maintenance', 'تحت الصيانة'),
    )

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='properties')
    title = models.CharField(max_length=200)
    description = models.TextField()
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    address = models.TextField()
    city = models.CharField(max_length=100)
    area = models.FloatField(help_text="المساحة بالمتر المربع")
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.city}"

    class Meta:
        verbose_name = "عقار"
        verbose_name_plural = "العقارات"

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='properties/')
    is_main = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"صورة {self.property.title}"

    class Meta:
        verbose_name = "صورة العقار"
        verbose_name_plural = "صور العقارات"

class PropertyRequest(models.Model):
    """طلب عرض عقار من المالك"""
    STATUS_CHOICES = (
        ('pending', 'في الانتظار'),
        ('approved', 'مقبول'),
        ('rejected', 'مرفوض'),
    )

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='property_requests')
    title = models.CharField(max_length=200)
    description = models.TextField()
    property_type = models.CharField(max_length=20, choices=Property.PROPERTY_TYPES)
    address = models.TextField()
    city = models.CharField(max_length=100)
    area = models.FloatField(help_text="المساحة بالمتر المربع")
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    admin_notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"طلب عرض: {self.title} - {self.owner.username}"

    class Meta:
        verbose_name = "طلب عرض عقار"
        verbose_name_plural = "طلبات عرض العقارات"

class PropertyRequestImage(models.Model):
    property_request = models.ForeignKey(PropertyRequest, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_requests/')
    is_main = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"صورة طلب: {self.property_request.title}"

class RentalRequest(models.Model):
    """طلب إيجار من العميل"""
    STATUS_CHOICES = (
        ('pending', 'في الانتظار'),
        ('approved', 'مقبول'),
        ('rejected', 'مرفوض'),
        ('completed', 'مكتمل'),
    )

    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rental_requests')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='rental_requests')
    message = models.TextField(help_text="رسالة من العميل")
    preferred_start_date = models.DateField()
    duration_months = models.IntegerField(help_text="مدة الإيجار بالأشهر")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    admin_notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"طلب إيجار: {self.property.title} - {self.client.username}"

    class Meta:
        verbose_name = "طلب إيجار"
        verbose_name_plural = "طلبات الإيجار"
