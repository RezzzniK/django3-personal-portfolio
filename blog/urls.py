from django.urls import path
from . import views #because we already inside the same folder

app_name='blog'
urlpatterns=[
path('',views.all_blogs,name='all_blogs'),
path('<int:blog_id>/',views.detail,name='detail'),#adding path for blog with id


]
