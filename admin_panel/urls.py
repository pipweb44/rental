from django.urls import path
from . import views

app_name = 'admin_panel'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('property-requests/', views.property_requests, name='property_requests'),
    path('rental-requests/', views.rental_requests, name='rental_requests'),
    path('approve-property/<int:request_id>/', views.approve_property_request, name='approve_property_request'),
    path('reject-property/<int:request_id>/', views.reject_property_request, name='reject_property_request'),
    path('approve-rental/<int:request_id>/', views.approve_rental_request, name='approve_rental_request'),
    path('reject-rental/<int:request_id>/', views.reject_rental_request, name='reject_rental_request'),
]
