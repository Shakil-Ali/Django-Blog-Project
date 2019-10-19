"""sonar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Imports 
#from django.contrib import admin
#from django.urls import path

"""
urlpatterns = [
    path('admin/', admin.site.urls),
]
"""

########################################

# Imports
from django.conf.urls import url
from . import views

# Name Spacing this URL File
app_name = 'articles'

# URLs
urlpatterns = [
	url(r'^$', views.article_list, name="list"),
    url(r'^create/$', views.article_create, name="create"),	
    # Remember any new urls made need to be before this one, or it will be counted as a slug
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),
]

