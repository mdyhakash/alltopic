from django.shortcuts import render
from .models import Topic
from django.shortcuts import render, get_object_or_404
# Create your views here.

def home(request):
    topics=Topic.objects.all()
    context={
        'topics':topics,
    }
    return render(request, 'home.html', context=context)

def details(request,c_code):
    topic = get_object_or_404(Topic, c_code=c_code)
    return render(request, 'details.html',{'topic':topic})