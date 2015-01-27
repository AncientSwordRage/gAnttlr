from django import template
from gantt_charts.models import Task

register = template.Library()

register.filter('is_root_task', Task.is_root_task)