from django.db import models
from django.contrib import admin

class Category(models.Model):
        value=models.CharField(max_length=50)
	def __unicode__(self):
		return self.value


class BlogPost(models.Model):
	title=models.CharField(max_length=150)
	body=models.TextField()
	timestamp=models.DateTimeField()
	category=models.ManyToManyField(Category)
	def __unicode__(self):
		return self.title

