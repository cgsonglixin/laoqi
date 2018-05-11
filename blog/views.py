from django.shortcuts import render
from .models import *
# Create your views here.
def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request,'base.html',{'blogs':blogs})