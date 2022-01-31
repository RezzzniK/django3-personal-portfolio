"""personal_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include

#importing functioanlity for static URLs
from django.conf.urls.static import static
#importing settings.py to our urls to be able to use class variables
#from there
from django.conf import settings

#importing views to be able to access the portfolio files
from portfolio import views

urlpatterns = [
    #adding home page from portfolio
    path('',views.home, name='home'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls'))#including our blog's set of urls
]
#adding to our list of urls new static path

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
