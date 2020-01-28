from django import forms

from .models import Project, Objective, Member,Task

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name','description','private']

class ObjectiveForm(forms.ModelForm):
    class Meta:
        model = Objective
        fields = ['name','description','completed']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name','description','completed']

class MemberForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    class Meta:
        model = Member
        fields = ['username','team_leader','role']
class MemberRemovalForm(forms.Form):
    username = forms.CharField(max_length=100)
