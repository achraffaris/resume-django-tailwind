from django.shortcuts import render
from .models import Resume

def home(request):
    data = Resume.objects.all().first()
    context = {
        'data': data
    }
    return render(request, 'index.html', context)
