from django import forms
from .models import PropertyRequest, RentalRequest, PropertyRequestImage

class PropertyRequestForm(forms.ModelForm):
    class Meta:
        model = PropertyRequest
        fields = ['title', 'description', 'property_type', 'address', 'city', 
                 'area', 'bedrooms', 'bathrooms', 'price']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'عنوان العقار'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'وصف العقار'
            }),
            'property_type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'العنوان التفصيلي'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'المدينة'
            }),
            'area': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'المساحة بالمتر المربع'
            }),
            'bedrooms': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'عدد غرف النوم'
            }),
            'bathrooms': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'عدد دورات المياه'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'السعر الشهري'
            }),
        }

class RentalRequestForm(forms.ModelForm):
    class Meta:
        model = RentalRequest
        fields = ['message', 'preferred_start_date', 'duration_months']
        widgets = {
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'رسالة للمالك'
            }),
            'preferred_start_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'duration_months': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'مدة الإيجار بالأشهر'
            }),
        }

class PropertyRequestImageForm(forms.ModelForm):
    class Meta:
        model = PropertyRequestImage
        fields = ['image', 'is_main']
        widgets = {
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
            'is_main': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
