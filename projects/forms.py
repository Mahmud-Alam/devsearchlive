from django.db import models
from django.forms import ModelForm, fields
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['vote_total','vote_ratio']