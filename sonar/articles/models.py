# Import statements
from django.db import models
from django.contrib.auth.models import User

# Comands for migration after editing a Model
# python manage.py makemigrations
# python manage.py migrate

# Create your models here.
class Article(models.Model):
	title =  models.CharField(max_length=100)
	slug = models.SlugField()
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default='default.png',blank=True)
	author = models.ForeignKey(User,on_delete=models.CASCADE,default=None)


# Function to make shell objects have title displayed instead of object
	def __str__(self):
		return self.title

	def snippet(self):
		return self.body[:50] + '...'



