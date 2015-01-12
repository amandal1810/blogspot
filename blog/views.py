from django.shortcuts import render
from blog.models import *
from django.core.paginator import *
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django import forms
from blog.forms import *
# Create your views here.

def all_blogs(request):
	posts = Post.objects.all().order_by("-created")
	paginator = Paginator(posts, 3)
	
	try: page = request.GET.get('page', '1')
	except ValueError: page = 1
	
	try: posts = paginator.page(page)
	except (InvalidPage, EmptyPage): posts = paginator.page(paginator.num_pages)
	
	return render(request,'blog/blog.html', { 'posts':posts, 'user':request.user })
	
	
def post(request,pk):
	post = Post.objects.get(pk=pk)
	comments = Comment.objects.filter(post=post)
	form = CommentForm()
	ct = { 'post':post, 'comments':comments, 'form':form }
	#ct.update(csrf(request))
	return render(request,'blog/post.html',ct)

def add_comment(request,pk):
	form = CommentForm(request.POST)
	print pk
	if form.is_valid():
		author = form.cleaned_data['author']
		body = form.cleaned_data['body']
	comment = Comment(author=author,body=body,post=Post.objects.get(pk=pk))
	comment.save()
	return HttpResponseRedirect(reverse("post", args=[pk]))
