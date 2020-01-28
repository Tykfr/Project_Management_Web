from django.db import models
from django.conf import settings
from django.shortcuts import reverse, get_object_or_404

# Create your models here.
"""
    Project model

    serves to hold the project information
"""
class Project(models.Model):
    boss = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    private = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def save(self,*args,**kwargs):
        project = super(Project,self).save(*args,**kwargs)
        ProjectHistory.objects.create(name = self.name,
        description=self.description,
        project=self)

    def get_absolute_url(self):
        return reverse('project-detail',kwargs={'project':self.pk})


"""
    Project Update Model

    used to store updates to the project
"""
class ProjectHistory(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    revision = models.IntegerField()

    def save(self,*args,**kwargs):
        self.revision = ProjectHistory.objects.filter(project=self.project).count() + 1
        super(ProjectHistory,self).save()

    class Meta:
        ordering = ['-revision']
"""
    Objective model

    server to add objectives to the project and add  group members
"""
class Objective(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Member',blank=True)
    completed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now=True)

    def save(self,*args,**kwargs):
        objective = super(Objective,self).save(*args,**kwargs)
        ObjectiveHistory.objects.create(name = self.name,
        description=self.description,
        objective=self)

    def get_absolute_url(self):
        return reverse('objective-detail',kwargs={'project':self.project.pk,'objective':self.pk})

"""
    Objective History Model

    used to store updates to objectives
"""

class ObjectiveHistory(models.Model):
    objective = models.ForeignKey(Objective,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    revision = models.IntegerField(default=0)

    def save(self,*args,**kwargs):
        self.revision = ObjectiveHistory.objects.filter(objective=self.objective).count() + 1
        super(ObjectiveHistory,self).save()

    class Meta:
        ordering = ['-revision']

"""
    Task Model

    serves to add mini objectives to each objective
    allows people to split work into smaller pieces
"""
class Task(models.Model):
    objective = models.ForeignKey(Objective,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('task-detail',kwargs={"objective":self.objective.pk,"task":self.pk})
"""
    Member model

    serves to connect the objective with the group members
"""

class Member(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    project_objective = models.ForeignKey(Objective,on_delete=models.CASCADE)
    team_leader = models.BooleanField(default=False)
    role = models.CharField(max_length=200,blank=True)
    task = models.ForeignKey(Task,on_delete=models.CASCADE,blank=True,null=True)

    def get_absolute_url(self):
        return reverse("objective-detail",kwargs={'project':self.project_objective.project.pk,'objective':self.project_objective.pk})
