from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Mahmud Alam's website!")

# def projects(request):
#     return HttpResponse('This is our projects page')

def projects(request):
    return render(request, 'projects/projects.html')


#def project(request,pk):
#    return HttpResponse('Project page: '+str(pk))

def project(request,pk):
    return render(request, 'projects/single-project.html')
