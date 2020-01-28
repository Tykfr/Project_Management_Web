from django.shortcuts import render,reverse,redirect, get_object_or_404,get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse_lazy
from django.views import View
from django.utils.decorators import method_decorator


from .models import Project, Objective, Member, ObjectiveHistory, ProjectHistory,Task
from .forms import ProjectForm, ObjectiveForm, MemberForm, MemberRemovalForm,TaskForm

"""

    Homepage of website if not logged in 

"""

class HomepageView(View):
        def get(self,request,*args,**kwargs):
            # if request.user.is_authenticated:
            return redirect('projects')

            # return render(request,'collab/homepage.html')


""" 
    Project  
    Used to edit at the project level
    Create, Update, Delete,List and View Details of projects

"""

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm

    @method_decorator(login_required)
    def dispatch(self,*args,**kwargs):
        return super().dispatch(*args,**kwargs)

    def get(self,request,*args,**kwargs):
        project_form = ProjectForm()
        content = {
        "project_form":project_form,
        }
        return render(request,'collab/project_form.html',content)

    # Url dispatcher using keyword project instead of default pk
    def get_object(self,*args,**kwargs):
        return Project.objects.get(pk=self.kwargs['project'])

    def form_valid(self,form):
        form.instance.boss = self.request.user
        return super(ProjectCreateView,self).form_valid(form)

class ProjectListView(ListView):
    model = Project

class ProjectDetailView(DetailView):
    model = Project

    def get_object(self,*args,**kwargs):
        return Project.objects.get(pk=self.kwargs['project'])

class ProjectUpdateView(View):

    def get(self,request,*args,**kwargs):
        project = get_object_or_404(Project,pk=self.kwargs['project'])
        project_form = ProjectForm(instance=project)
        content = {
        "project_form":project_form,
        "project":project,
        }
        return render(request,'collab/project_form.html',content)

    def post(self,request,*args,**kwargs):
        project = get_object_or_404(Project,pk=self.kwargs['project'])
        project_form = ProjectForm(request.POST,instance=project)

        if project_form.is_valid():
            project_form.save()
            return redirect(reverse('project-detail',kwargs={"project":self.kwargs["project"]}))
        content = {
        "project_form":project_form,
        "project":project,
        }
        return render(request,'collab/project_form.html',content)

class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy("projects")
    #Url using project as variable name so get_object must look for project instead of the default pk
    def get_object(self,*args,**kwargs):
        return Project.objects.get(pk=self.kwargs['project'])


    def delete(self,*args,**kwargs):
        project_history = ProjectHistory.objects.filter(project=get_object_or_404(Project,pk=self.kwargs['project']))
        project_history.delete()
        return super(ProjectDeleteView,self).delete(*args,**kwargs)

"""
    Objective View 
    Level Below every project used to create smaller goals
    Create,Update,Delete,List and Detail of objective section


"""
class ObjectiveListView(ListView):
    model = Objective

class ObjectiveDetailView(DetailView):
    model = Objective

    #Url using objective as variable name so get_object must look for project instead of the default pk
    def get_object(self,*args,**kwargs):
        return Objective.objects.get(pk=self.kwargs['objective'])


class ObjectiveCreateView(CreateView):
    model = Objective
    form_class = ObjectiveForm

    #Url using objective as variable name so get_object must look for project instead of the default pk
    def get_object(self,*args,**kwargs):
        return Objective.objects.get(pk=self.kwargs['objective'])

    def form_valid(self,form):
        form.instance.project = get_object_or_404(Project,pk=self.kwargs['project'])
        return super(ObjectiveCreateView,self).form_valid(form)

class ObjectiveUpdateView(View):

    def get(self,request,*args,**kwargs):
        objective = get_object_or_404(Objective,pk=self.kwargs['objective'])
        form = ObjectiveForm(instance=objective)
        content = {
        "form":form,
        "objective":objective,
        }
        return render(request,'collab/objective_form.html',content)

    def post(self,request,*args,**kwargs):
        objective = get_object_or_404(Objective,pk=self.kwargs['objective'])
        form = ObjectiveForm(request.POST,instance=objective)

        if form.is_valid():
            form.save()
            return redirect(reverse('objective-detail',kwargs={'project':objective.project.pk,"objective":objective.pk}))
        content = {
        "form":form,
        "objective":objective,
        }
        return render(request,'collab/objective_form.html',content)

class ObjectiveDeleteView(DeleteView):
    model = Objective
    success_url = reverse_lazy('projects')

    #Url using objective as variable name so get_object must look for project instead of the default pk
    def get_object(self,*args,**kwargs):
        return Objective.objects.get(pk=self.kwargs['objective'])

    def delete(self,*args,**kwargs):
        ObjectiveHistory.objects.filter(objective=get_object_or_404(Objective,pk=self.kwargs['objective'])).delete()
        return super(ObjectiveDeleteView,self).delete(*args,**kwargs)

"""

    Task View 
    Used to create small task for each objective that can be completed
    All functionality of task, used to show progress of objectives
    

"""

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm

    def form_valid(self,form):
        form.instance.objective = get_object_or_404(Objective,pk=self.kwargs['objective'])
        return super(TaskCreateView,self).form_valid(form)

class TaskDetailView(DetailView):
    model = Task

    def get_object(self,*args,**kwargs):
        return Task.objects.get(pk=self.kwargs['task'])

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm

    def get_object(self,*args,**kwargs):
        return Task.objects.get(pk=self.kwargs['task'])

class TaskDeleteView(DeleteView):
    model = Task

    def get_object(self,*args,**kwargs):
        return Task.objects.get(pk=self.kwargs['task'])

"""

        Member View 
        Used to group members into different projects and assign tasks
        Members details,creation and delete view

"""

class MemberCreateView(CreateView):
    model = Member
    form_class = MemberForm

    #Url using objective as variable name so get_object must look for project instead of the default pk
    def get_object(self,*args,**kwargs):
        return Member.objects.get(pk=self.kwargs['objective'])

    def post(self,request,*args,**kwargs):
        form = MemberForm(request.POST)
        if form.is_valid():
            user = self.form_valid(form)
            return redirect(reverse("objective-detail",kwargs={'project':self.kwargs['project'],'objective':self.kwargs['objective']}))

        return render(request,'collab/member_form.html',{'form':form})

    def form_valid(self,form):
        form.instance.user = get_object_or_404(get_user_model(),username=form.cleaned_data.get('username'))
        form.instance.project_objective =  get_object_or_404(Objective,pk=self.kwargs['objective'])
        return super(MemberCreateView,self).form_valid(form)
"""

    MemberDeleteView uses a custom removal form so that users can
    enter username and the post method will look for that user and delete if found

"""
class MemberDeleteView(View):
    model = Member

    def get(self,request,*args,**kwargs):
        form = MemberRemovalForm
        return render(request,'collab/member_confirm_delete.html',{'form':form})

    def post(self,request,*args,**kwargs):
        form = MemberRemovalForm(request.POST)
        if form.is_valid():
            username = get_object_or_404(get_user_model(),username=form.cleaned_data.get('username'))
            objective = get_object_or_404(Objective,pk=self.kwargs['objective'])
            member = Member.objects.filter(user=username,project_objective=objective)
            for m in member:
                objective.members.remove(m.user)
            return redirect(reverse("objective-detail",kwargs={'project':self.kwargs['project'],'objective':self.kwargs['objective']}))

        return render(request,'collab/member_confirm_delete.html',{'form':form})

class MemberDetailView(DetailView):
    model = Member
