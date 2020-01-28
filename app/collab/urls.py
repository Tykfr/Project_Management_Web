from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomepageView.as_view(),name='homepage'),
    path('projects/',views.ProjectListView.as_view(),name='projects'),
    path('create-project/',views.ProjectCreateView.as_view(),name='create-project'),
    path('project-<int:project>/',views.ProjectDetailView.as_view(),name='project-detail'),
    path('project-<int:project>-update/',views.ProjectUpdateView.as_view(),name='update-project'),
    path('project-<int:project>-delete/',views.ProjectDeleteView.as_view(),name='delete-project'),
    path('project-<int:project>/create-objective',views.ObjectiveCreateView.as_view(),name='create-objective'),
    path('project-<int:project>/objective-<int:objective>/',views.ObjectiveDetailView.as_view(),name='objective-detail'),
    path('project-<int:project>/objective-<int:objective>-update/',views.ObjectiveUpdateView.as_view(),name='update-objective'),
    path('project-<int:project>/objective-<int:objective>-delete/',views.ObjectiveDeleteView.as_view(),name='delete-objective'),
    path('project/objective-<int:objective>/task-create/',views.TaskCreateView.as_view(),name='create-task'),
    path('project/objective-<int:objective>/task-<int:task>/',views.TaskDetailView.as_view(),name='task-detail'),
    path('project/objective-<int:objective>/task-<int:task>/',views.TaskUpdateView.as_view(),name='update-task'),
    path('project/objective-<int:objective>-delete/task-<int:task>/',views.TaskDeleteView.as_view(),name='delete-task'),
    path('project-<int:project>/objective-<int:objective>/add-member/',views.MemberCreateView.as_view(),name='add-member'),
    path('project-<int:project>/objective-<int:objective>/remove-member/',views.MemberDeleteView.as_view(),name='remove-member'),

]
