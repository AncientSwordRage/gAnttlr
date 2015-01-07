from django.db import models
from django.utils.encoding import smart_unicode
from django.template.defaultfilters import slugify

# Create your models here.

class Project(models.Model):
	owner = models.ForeignKey('auth.User')
	title = models.CharField(max_length=100)
	slug =  models.SlugField(unique=True)
	created_date = models.DateTimeField(auto_now_add=True, auto_now = False)
	updated_date = models.DateTimeField(auto_now_add=False, auto_now = True)


	def __str__(self):
		return smart_unicode(self.title)

	def save(self):
		super(Project, self).save()
		self.slug = '{slugged_title}-{id}'.format(id=self.id, slugged_title=slugify(self.title))
		super(Project,self).save()


