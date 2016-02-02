from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import User
# Create your views here.
from .forms import PostForm
from .models import Post, Categories

@login_required
def post_create(request):
	if not request.user.is_authenticated:
		raise Http404

	form = PostForm(request.POST or None, request.FILES or None)
	print(request.user.id)
	mUser = User.objects.get(pk=request.user.id)
	print(mUser)
	if form.is_valid():
		instance = form.save(commit=False)
		if request.user.is_authenticated:
			instance.author = mUser
		instance.save()
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())

	heading = "Make a post"
	subheading = "Share with the World."
	context = {
		'heading': heading,
		'subheading': subheading,
		"form": form,
	}
	return render(request, "blog/post_form.html", context)

def post_detail(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	context = {
		"post": instance,
	}
	return render(request, "blog/post_detail.html", context)

@login_required
def post_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	post_to_be_changed = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=post_to_be_changed)
	
	if form.is_valid():
		post_to_be_changed = form.save(commit=False)
		post_to_be_changed.save()
		return HttpResponseRedirect(post_to_be_changed.get_absolute_url())

	heading = "Update your post"
	subheading = "Don't forget you check your spelling"
	context = {
		'heading': heading,
		'subheading': subheading,
		'post_to_be_changed': post_to_be_changed,
		'form': form,
	}
	return render(request, 'blog/post_form.html', context)

@login_required
def post_delete(request, slug=None):
	post = get_object_or_404(Post, slug=slug).delete()
	posts = Post.objects.all()
	context = {
		'posts': posts,
	}
	return render(request, 'main/index.html', context)



