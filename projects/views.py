from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website',
        'topRated': True
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work',
        'topRated': False
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community',
        'topRated': True
    }
]

def home(request):
    return HttpResponse("Welcome to Mahmud Alam's website!")

#1 def projects(request):
#     return HttpResponse('This is our projects page')

#2 def projects(request):
#     #name = 'Mahmud Alam'
#     #age  = 22
#     #context = {'name':name,'age':age}
#     context = {'projects':projectsList}
#     return render(request, 'projects/projects.html',context)

def projects(request):
    projects = Project.objects.all()
    #print('PROJECT:',projects)
    context = {'projects':projects}
    return render(request, 'projects/projects.html',context)




# def project(request,pk):
#    return HttpResponse('Project page: '+str(pk))

#def project(request,pk):
#    return render(request, 'projects/single-project.html')

# def project(request, pk):
#     projectObject = None
#     for i in projectsList:
#         if i['id'] == pk:
#             projectObject = i
#     return render(request, 'projects/single-project.html',{'project':projectObject})


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    # new added line tags
    #tags = projectObj.tags.all()
    #reviews = projectObj.review_set.all()
    #context = {'project':projectObj, 'tags':tags,'reviews':reviews}
    context = {'project':projectObj}
    return render(request, 'projects/single-project.html',context)
    