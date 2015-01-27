# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dependency',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('completed', models.BooleanField(default=False)),
                ('project', models.ForeignKey(to='gantt_charts.Project', related_name='tasks')),
                ('subtasks', models.ManyToManyField(to='gantt_charts.Task', blank=True, through='gantt_charts.Dependency', related_name='supertasks', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='dependency',
            name='subtask',
            field=models.ForeignKey(to='gantt_charts.Task', related_name='dependencies_as_subtask'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dependency',
            name='supertask',
            field=models.ForeignKey(to='gantt_charts.Task', related_name='dependencies_as_supertask'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='dependency',
            unique_together=set([('supertask', 'subtask')]),
        ),
    ]
