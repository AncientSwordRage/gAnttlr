# Disable the two few methods complaint
# pylint: disable=R0903

from django.db import models
from django.template.defaultfilters import slugify
from django import template
register = template.Library()

# Create your models here.

class Project(models.Model):
    owner = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        super(Project, self, **kwargs).save()
        self.slug = slugify(self.title)
        super(Project, self, **kwargs).save()
        
    def create(self):
        pass


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    project = models.ForeignKey('Project', related_name="tasks")
    subtasks = models.ManyToManyField('self', 
                                      through='Dependency',
                                      symmetrical=False,
                                      through_fields=('supertask', 'subtask'),
                                      related_name='supertasks',
                                      null=True,
                                      blank=True)

    def all_sub_tasks(self, **kwargs):
        qs = self.subtasks.filter(**kwargs)
        for sub_task in qs:
            qs = qs | sub_task.sub_tasks(**kwargs)
        return qs

    def is_root_task(self, root=None):
        '''Returns true if the task is the root of a series of other tasks'''
        if root:
            # except for where the task is my 'parent'
            # Are their no dependencies where I am the Sub-Task,
            return not self.supertasks.exclude(task_id__exact=root.id).exists()
        else:
            # Are their no dependencies where I am the Sub-Task
            return not self.supertasks.exists()

    def __str__(self):
        return self.title


class Dependency(models.Model):
    supertask = models.ForeignKey(Task, related_name='dependencies_as_supertask')
    subtask = models.ForeignKey(Task, related_name='dependencies_as_subtask')

    class Meta:
        unique_together = ('supertask', 'subtask')


    def __str__(self):
        return self.task.title+ " depends on "+ self.sub_task.title
