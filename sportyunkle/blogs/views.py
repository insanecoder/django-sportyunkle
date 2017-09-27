from django.shortcuts import render
from .models import BlogPost
from .forms import PostForm
from .models import Tag
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import HttpResponse
import pprint
from pprint import pprint as pr

def add_blog(request,pk):
	# return HttpResponse(str(pk))
	
	# return HttpResponse(str(post))
	#form= PostForm()
	if pk:
		post = get_object_or_404(BlogPost,id=pk)
		form = PostForm(instance=post)
	else:
		form= PostForm()
	return render(request, 'post_blog.html', {'form': form,'id':pk })

def save_blog(request):
	id= request.GET.get("ID",'')
	tagID= request.GET.get("tags",'')
	tagObj= Tag.objects.filter(id=tagID).get()
	if id:
		f= get_object_or_404(BlogPost,id=id)
		f= PostForm(request.GET,instance=f)
		f.save()
	else:
		form= PostForm(request.GET)
		blogPost= form.save()
	return render(request, 'save_blog.html', {})

def home_page(request):
	return render(request, 'home_page.html', {})