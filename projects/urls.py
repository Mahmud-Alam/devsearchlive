from django.urls import path
from . import views

urlpatterns = [
    #path('',views.home),
    #path('projects/',views.projects),
    path('',views.projects),
    path('project/<str:pk>/',views.project, name='project'),
]