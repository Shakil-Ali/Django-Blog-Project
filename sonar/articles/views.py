# Imports
from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Functions (Views)

# Function to view all articles
def article_list(request):
	articles = Article.objects.all().order_by('date')
	return render(request, 'articles/article_list.html', { 'articles': articles })

# Function to display article content/properties
def article_detail(request, slug):
	# return HttpResponse(slug)
	article = Article.objects.get(slug=slug)
	return render(request, 'articles/article_detail.html', { 'article':article })

# Decorator to check if logged in
@login_required(login_url="/accounts/login/")
# Function to create article
def article_create(request):
	if request.method == 'POST':
		form = forms.CreateArticle(request.POST, request.FILES)
		if form.is_valid():
			# Save article to DB
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			return redirect('articles:list')
	else:
		form = forms.CreateArticle()
	return render(request, 'articles/article_create.html', { 'form': form })




