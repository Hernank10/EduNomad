from django.shortcuts import render
from apps.language_practice.models import Course

def home(request):
    # Mostramos los 3 cursos más recientes en la home
    featured_courses = Course.objects.all()[:3]
    return render(request, 'core/home.html', {'courses': featured_courses})
