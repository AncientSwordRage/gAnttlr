from django.contrib import admin
from gantt_charts.models import Project,Task

class ProjectAdmin(admin.ModelAdmin):
	fields = ['owner','title']

# Register your models here.
admin.site.register(Project,ProjectAdmin)
admin.site.register(Task)