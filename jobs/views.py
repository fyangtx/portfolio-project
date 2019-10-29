from django.shortcuts import render
from .models import Job

# Create your views here.
def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})

def Blog(request):
    jobs = Job.objects
    return render(request, 'blog/allblogs.html', {'blog':jobs})    