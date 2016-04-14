try:
	from urllib.parse import quote_plus #python 3
except:
	pass

from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import User
# Structure Imports here.
from .forms import PostForm
from .models import Post, Categories
from .utils import get_read_time
from comments.forms import CommentForm
from comments.models import Comment

# Create your classes here.
from rest_framework import viewsets
from .serializers import CategorySerializer, PostSerializer

class CategoriesViewSet(viewsets.ModelViewSet):
	queryset = Categories.objects.all().order_by('id')
	serializer_class = CategorySerializer

class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all().order_by('id')
	serializer_class = PostSerializer

# Create your views here.
@login_required
def post_create(request):
	if not request.user.is_authenticated:
		raise Http404

	form = PostForm(request.POST or None, request.FILES or None)
	mUser = User.objects.get(pk=request.user.id)
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
	if instance.publish > timezone.now().date() or instance.draft:
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	share_string = quote_plus(instance.content)

	read_time = get_read_time(instance.get_markdown())

	initial_data = {
	"content_type": instance.get_content_type,
	"object_id": instance.id
	}
	form = CommentForm(request.POST or None, initial=initial_data)
	if form.is_valid():
		c_type = form.cleaned_data.get("content_type")
		content_type = ContentType.objects.get(model=c_type)
		obj_id = form.cleaned_data.get('object_id')
		content_data = form.cleaned_data.get("content")
		parent_obj = None
		try:
			parent_id = int(request.POST.get("parent_id"))
		except:
			parent_id = None
			
		if parent_id:
			parent_qs = Comment.objects.filter(id=parent_id)
			if parent_qs.exists() and parent_qs.count() == 1:
				parent_obj = parent_qs.first()
		new_comment, created = Comment.objects.get_or_create(
									user = request.user,
									content_type= content_type,
									object_id = obj_id,
									content = content_data,
									parent = parent_obj,
									)
		return HttpResponseRedirect(new_comment.content_object.get_absolute_url())
	comments = instance.comments
	context = {
	"title": instance.title,
	"post": instance,
	"share_string": share_string,
	"comments": comments,
	"comment_form":form,
	"read_time": read_time,
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
	subheading = "Don't forget to check your spelling"
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



