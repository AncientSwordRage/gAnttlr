# Disable the two few methods complaint
# pylint: disable=R0903

from django import forms

from .models import Project, Task, Dependency

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('title',)

class TaskForm(forms.ModelForm):
    subtasks = forms.ModelMultipleChoiceField(queryset=Task.objects.none(), required=False)

    class Meta:
        model = Task
        exclude = ('project', 'subtasks', )

    def save(self, commit=False):
        instance = forms.ModelForm.save(self)
        instance.subtasks.clear()
        for subtask in self.cleaned_data['subtasks']:
            Dependency.objects.create(supertask=instance, subtask=subtask)

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['subtasks'].queryset = Task.objects.filter(
                                               project=self.instance.project).exclude(pk=self.instance.pk)

        # Set intial selected sub-tasks
        if 'instance' in kwargs:
            initial = kwargs.setdefault('initial', {})
            initial['subtasks'] = [t.subtask.pk for t in kwargs['instance'].dependencies_as_supertask.all()]
