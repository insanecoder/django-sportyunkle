from django.db import models
from django.utils import timezone
from pprint import pprint as pr


class Tag(models.Model):
	tagName= models.CharField(max_length=100)

class BlogPost(models.Model):
	creatorID = models.ForeignKey('User',on_delete=models.CASCADE )
	blogContent= models.TextField()
	title = models.CharField(max_length=200)
	seoTitle = models.CharField(max_length=200)
	seoDescription= models.CharField(max_length=200)
	imgPath= models.CharField(max_length=200)
	created_date = models.DateTimeField(default=timezone.now)
	update_date = models.DateTimeField(auto_now=True)
	tags= models.ManyToManyField(Tag)
	def get_fields(self):
		return [(field.name, field.value_to_string(self)) for field in BlogPost._meta.fields]
	def save(self, commit=True):
		pr(self.t._meta)
		for name in self.t._meta.get_fields():
			self.tags.add(self.t.name)
		if commit:
			self.save()
		return self


class User(models.Model):
	userName= models.CharField(max_length=200)
	def __str__(self):
		a=u'{0}'.format(self.userName)
		return "Dummu "+a



