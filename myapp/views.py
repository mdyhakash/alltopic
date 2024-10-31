from django.shortcuts import render
from .models import Topic
# Create your views here.

def home(request):
    topics=Topic.objects.all()
    context={
        'topics':topics,
    }
    return render(request, 'home.html', context=context)