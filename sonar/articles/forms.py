# Imports
from django import forms
from . import models

# Class
class CreateArticle(forms.ModelForm):
	class Meta:
		model = models.Article
		fields = ['title', 'body', 'slug', 'thumb']
		

