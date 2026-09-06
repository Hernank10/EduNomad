from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def dashboard(request):
    return render(request, 'lms/dashboard.html')

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('admin/', admin.site.urls),
    path('api/', include('apps.core.urls')),
]
