from django.urls import path
from . import views

app_name = 'properties'

urlpatterns = [
    path('', views.home, name='home'),
    path('properties/', views.property_list, name='property_list'),
    path('property/<int:pk>/', views.property_detail, name='property_detail'),
    path('rent-request/<int:property_id>/', views.rent_request, name='rent_request'),
    path('add-property-request/', views.add_property_request, name='add_property_request'),
    path('my-requests/', views.my_requests, name='my_requests'),
    path('my-properties/', views.my_properties, name='my_properties'),
]
