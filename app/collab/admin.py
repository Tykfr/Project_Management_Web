from django.contrib import admin
from .models import Project, Objective, Member
# Register your models here.
class ObjectiveInline(admin.TabularInline):
    model = Objective

class ProjectAdmin(admin.ModelAdmin):
    fields = ("boss",'name','description','private')
    list_display = ("name","created_on")
    list_filter = ("boss",'private')
    inlines = [
        ObjectiveInline,
    ]

admin.site.register(Project,ProjectAdmin)
admin.site.register(Member)
