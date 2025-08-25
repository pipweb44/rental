#!/usr/bin/env python
"""
Script to create sample data for the rental website
"""
import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from users.models import User
from properties.models import Property, PropertyRequest, RentalRequest, PropertyImage, PropertyRequestImage
from django.contrib.auth import get_user_model
from decimal import Decimal

def create_sample_users():
    """Create sample users"""
    print("Creating sample users...")
    
    # Create owners
    owner1, created = User.objects.get_or_create(
        username='owner1',
        defaults={
            'email': 'owner1@example.com',
            'first_name': 'أحمد',
            'last_name': 'محمد',
            'user_type': 'owner',
            'phone': '+966501234567',
            'address': 'الرياض، حي النخيل',
            'is_verified': True
        }
    )
    if created:
        owner1.set_password('password123')
        owner1.save()
    
    owner2, created = User.objects.get_or_create(
        username='owner2',
        defaults={
            'email': 'owner2@example.com',
            'first_name': 'فاطمة',
            'last_name': 'أحمد',
            'user_type': 'owner',
            'phone': '+966507654321',
            'address': 'جدة، حي الصفا',
            'is_verified': True
        }
    )
    if created:
        owner2.set_password('password123')
        owner2.save()
    
    # Create clients
    client1, created = User.objects.get_or_create(
        username='client1',
        defaults={
            'email': 'client1@example.com',
            'first_name': 'خالد',
            'last_name': 'سالم',
            'user_type': 'client',
            'phone': '+966551234567',
            'address': 'الدمام، حي الفيصلية',
            'is_verified': True
        }
    )
    if created:
        client1.set_password('password123')
        client1.save()
    
    client2, created = User.objects.get_or_create(
        username='client2',
        defaults={
            'email': 'client2@example.com',
            'first_name': 'نورا',
            'last_name': 'علي',
            'user_type': 'client',
            'phone': '+966557654321',
            'address': 'مكة، حي العزيزية',
            'is_verified': True
        }
    )
    if created:
        client2.set_password('password123')
        client2.save()
    
    return owner1, owner2, client1, client2

def create_sample_properties(owner1, owner2):
    """Create sample properties"""
    print("Creating sample properties...")
    
    properties_data = [
        {
            'owner': owner1,
            'title': 'شقة فاخرة في حي النخيل',
            'description': 'شقة مفروشة بالكامل في موقع متميز، تحتوي على جميع الخدمات والمرافق الحديثة. قريبة من المدارس والمستشفيات ومراكز التسوق.',
            'property_type': 'apartment',
            'address': 'شارع الملك فهد، حي النخيل، الرياض',
            'city': 'الرياض',
            'area': 120.5,
            'bedrooms': 3,
            'bathrooms': 2,
            'price': Decimal('2500.00'),
            'status': 'available',
            'is_approved': True
        },
        {
            'owner': owner1,
            'title': 'فيلا عائلية في حي الملك فهد',
            'description': 'فيلا واسعة مع حديقة خاصة ومسبح، مثالية للعائلات الكبيرة. تتميز بالتصميم العصري والمساحات الواسعة.',
            'property_type': 'villa',
            'address': 'حي الملك فهد، الرياض',
            'city': 'الرياض',
            'area': 350.0,
            'bedrooms': 5,
            'bathrooms': 4,
            'price': Decimal('8000.00'),
            'status': 'available',
            'is_approved': True
        },
        {
            'owner': owner2,
            'title': 'مكتب تجاري في وسط جدة',
            'description': 'مكتب في موقع استراتيجي في وسط جدة، مناسب للشركات والمكاتب التجارية. يحتوي على مواقف سيارات وأمن على مدار الساعة.',
            'property_type': 'office',
            'address': 'شارع التحلية، وسط جدة',
            'city': 'جدة',
            'area': 80.0,
            'bedrooms': 0,
            'bathrooms': 2,
            'price': Decimal('3500.00'),
            'status': 'available',
            'is_approved': True
        },
        {
            'owner': owner2,
            'title': 'شقة بإطلالة بحرية في جدة',
            'description': 'شقة مميزة بإطلالة رائعة على البحر الأحمر، مفروشة بالكامل مع شرفة واسعة. في برج سكني حديث مع جميع الخدمات.',
            'property_type': 'apartment',
            'address': 'كورنيش جدة، حي الشاطئ',
            'city': 'جدة',
            'area': 95.0,
            'bedrooms': 2,
            'bathrooms': 2,
            'price': Decimal('4200.00'),
            'status': 'available',
            'is_approved': True
        },
        {
            'owner': owner1,
            'title': 'محل تجاري في شارع رئيسي',
            'description': 'محل تجاري في موقع حيوي على شارع رئيسي، مناسب لجميع أنواع التجارة. مساحة واسعة مع واجهة زجاجية مميزة.',
            'property_type': 'shop',
            'address': 'شارع العليا الرئيسي، الرياض',
            'city': 'الرياض',
            'area': 60.0,
            'bedrooms': 0,
            'bathrooms': 1,
            'price': Decimal('5500.00'),
            'status': 'available',
            'is_approved': True
        }
    ]
    
    created_properties = []
    for prop_data in properties_data:
        property_obj, created = Property.objects.get_or_create(
            title=prop_data['title'],
            defaults=prop_data
        )
        created_properties.append(property_obj)
        if created:
            print(f"Created property: {property_obj.title}")
    
    return created_properties

def create_sample_property_requests(owner1, owner2):
    """Create sample property requests"""
    print("Creating sample property requests...")
    
    requests_data = [
        {
            'owner': owner1,
            'title': 'شقة في حي الياسمين',
            'description': 'شقة عائلية في حي هادئ ومميز، قريبة من الخدمات الأساسية.',
            'property_type': 'apartment',
            'address': 'حي الياسمين، الرياض',
            'city': 'الرياض',
            'area': 110.0,
            'bedrooms': 3,
            'bathrooms': 2,
            'price': Decimal('2800.00'),
            'status': 'pending'
        },
        {
            'owner': owner2,
            'title': 'مستودع في المنطقة الصناعية',
            'description': 'مستودع واسع مناسب للتخزين والأنشطة الصناعية.',
            'property_type': 'warehouse',
            'address': 'المنطقة الصناعية الثانية، جدة',
            'city': 'جدة',
            'area': 500.0,
            'bedrooms': 0,
            'bathrooms': 2,
            'price': Decimal('6000.00'),
            'status': 'pending'
        }
    ]
    
    created_requests = []
    for req_data in requests_data:
        request_obj, created = PropertyRequest.objects.get_or_create(
            title=req_data['title'],
            defaults=req_data
        )
        created_requests.append(request_obj)
        if created:
            print(f"Created property request: {request_obj.title}")
    
    return created_requests

def create_sample_rental_requests(properties, client1, client2):
    """Create sample rental requests"""
    print("Creating sample rental requests...")
    
    from datetime import date, timedelta
    
    requests_data = [
        {
            'client': client1,
            'property': properties[0],  # شقة فاخرة في حي النخيل
            'message': 'أهلاً، أنا مهتم بإيجار هذه الشقة لعائلتي. نحن عائلة مكونة من 4 أفراد ونبحث عن سكن في موقع متميز. أرجو التواصل معي لمناقشة التفاصيل.',
            'preferred_start_date': date.today() + timedelta(days=30),
            'duration_months': 12,
            'status': 'pending'
        },
        {
            'client': client2,
            'property': properties[1],  # فيلا عائلية
            'message': 'السلام عليكم، أرغب في استئجار هذه الفيلا لعائلة كبيرة. الموقع والمواصفات مناسبة جداً لاحتياجاتنا. هل يمكن ترتيب موعد للمعاينة؟',
            'preferred_start_date': date.today() + timedelta(days=45),
            'duration_months': 24,
            'status': 'pending'
        },
        {
            'client': client1,
            'property': properties[2],  # مكتب تجاري
            'message': 'مرحباً، أبحث عن مكتب لشركتي الناشئة. هذا المكتب يبدو مناسباً من حيث الموقع والمساحة. أرجو إرسال المزيد من التفاصيل.',
            'preferred_start_date': date.today() + timedelta(days=15),
            'duration_months': 18,
            'status': 'approved'
        }
    ]
    
    created_requests = []
    for req_data in requests_data:
        # Check if request already exists
        existing = RentalRequest.objects.filter(
            client=req_data['client'],
            property=req_data['property']
        ).first()
        
        if not existing:
            request_obj = RentalRequest.objects.create(**req_data)
            created_requests.append(request_obj)
            print(f"Created rental request: {request_obj.property.title} by {request_obj.client.username}")
    
    return created_requests

def main():
    """Main function to create all sample data"""
    print("Starting to create sample data...")
    
    # Create users
    owner1, owner2, client1, client2 = create_sample_users()
    
    # Create properties
    properties = create_sample_properties(owner1, owner2)
    
    # Create property requests
    property_requests = create_sample_property_requests(owner1, owner2)
    
    # Create rental requests
    rental_requests = create_sample_rental_requests(properties, client1, client2)
    
    print("\n" + "="*50)
    print("Sample data created successfully!")
    print("="*50)
    print(f"Users created: {User.objects.count()}")
    print(f"Properties created: {Property.objects.count()}")
    print(f"Property requests created: {PropertyRequest.objects.count()}")
    print(f"Rental requests created: {RentalRequest.objects.count()}")
    print("\nLogin credentials:")
    print("Admin: admin / admin123")
    print("Owner 1: owner1 / password123")
    print("Owner 2: owner2 / password123")
    print("Client 1: client1 / password123")
    print("Client 2: client2 / password123")
    print("="*50)

if __name__ == '__main__':
    main()
