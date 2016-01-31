from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.sitemaps import Sitemap
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.db.models import Q
from blog.models import Post, Categories
from django.core.urlresolvers import reverse
import datetime

# Create your views here.
def view_homepage(request, slug=None):
	posts_list = Post.objects.all().order_by("-id")
	categories_list = Categories.objects.all().order_by("id")

	# query = request.GET.get("q")
	# if query:
	# 	posts_list = posts_list.filter(
	# 		Q(title__icontains=query) |
	# 		Q(subtitle__icontains=query) |
	# 		Q(author__icontains=query) |
	# 		Q(article__icontains=query) |
	# 		Q(tags__icontains=query) |
	# 		Q(date_added__icontains=query)
	# 		)
	# paginator = Paginator(posts_list, 5)

	# page = request.GET.get('page')
	# try:
	# 	queryset = paginator.page(page)
	# except PageNotAnInteger:
	# 	queryset = paginator.page(1)
	# except EmptyPage:
	# 	queryset = paginator.page(paginator.num_pages)

	# title = "Search here"
	context = {
		#'posts': queryset,
		'posts': posts_list,
		'categories': categories_list,	
	}
	return render(request, 'main/index.html', context)

def post_like(request, slug=None):
	if request.user.is_authenticated:
		post = get_object_or_404(Post, slug=slug)
		post.likes += 1
		#post.likes.save()
		return HttpResponseRedirect(reverse('like', args=(post.slug,)))


#def view_homepage(request):
#	return render(request, 'main/index.html', {})

def view_aboutpage(request):
	return render(request, 'main/about.html', {})

# def view_contactpage(request):
# 	return render(request, 'main/contact.html', {})