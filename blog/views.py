from django.shortcuts import render,get_object_or_404
from .models import Blog

# Create your views here.
def all_blogs(request):
    blog_objects=Blog.objects.order_by('-date')#[:5]#sorting by date from most recent
                                                   # taking only first 5 blogs
    return render(request,'blog/all_blogs.html',{'blog_objects':blog_objects})

def detail (request,blog_id):#adding a function with request and id
                    #getting data from Blog table with primary key(pk)==blog_id
    blog=get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/detail.html',{'blog':blog})
                     #passing th url and blog from the db
