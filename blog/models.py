from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=60)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	author = models.CharField(max_length=40)
	
	def __unicode__(self):
		return self.title

class Comment(models.Model):
	author = models.CharField(max_length=40)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	post = models.ForeignKey(Post)
	
	def __unicode__(self):
		return self.body
