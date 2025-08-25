from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import UserRegistrationForm, UserProfileForm

def login_view(request):
    """تسجيل الدخول"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'تم تسجيل الدخول بنجاح!')
            return redirect('properties:home')
        else:
            messages.error(request, 'اسم المستخدم أو كلمة المرور غير صحيحة')

    return render(request, 'users/login.html')

def logout_view(request):
    """تسجيل الخروج"""
    logout(request)
    messages.success(request, 'تم تسجيل الخروج بنجاح!')
    return redirect('properties:home')

def register_view(request):
    """التسجيل"""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'تم إنشاء الحساب بنجاح!')
            return redirect('properties:home')
    else:
        form = UserRegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)

@login_required
def profile_view(request):
    """الملف الشخصي"""
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم تحديث الملف الشخصي بنجاح!')
            return redirect('users:profile')
    else:
        form = UserProfileForm(instance=request.user)

    # إحصائيات المستخدم
    if request.user.user_type == 'owner':
        total_properties = request.user.properties.count()
        active_properties = request.user.properties.filter(status='approved').count()
    else:
        total_properties = 0
        active_properties = 0

    context = {
        'form': form,
        'total_properties': total_properties,
        'active_properties': active_properties,
    }
    return render(request, 'users/profile.html', context)


@login_required
def edit_profile_view(request):
    """تعديل الملف الشخصي"""
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم تحديث الملف الشخصي بنجاح!')
            return redirect('users:profile')
    else:
        form = UserProfileForm(instance=request.user)

    context = {
        'form': form,
    }
    return render(request, 'users/edit_profile.html', context)


@login_required
def change_password_view(request):
    """تغيير كلمة المرور"""
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'تم تغيير كلمة المرور بنجاح!')
            return redirect('users:profile')
    else:
        form = PasswordChangeForm(request.user)

    context = {
        'form': form,
    }
    return render(request, 'users/change_password.html', context)
