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
from django.utils import timezone
import datetime
# Create your views here.
def view_homepage(request, slug=None):
	categories_list = Categories.objects.all().order_by("id")
	today = timezone.now().date()

	posts_list = Post.objects.active()
	if request.user.is_staff or request.user.is_superuser:
		posts_list = Post.objects.all()

	query = request.GET.get("q")
	if query:
		posts_list = posts_list.filter(
				Q(title__icontains=query)|
				Q(subtitle__icontains=query) |
				Q(content__icontains=query)
				)
	paginator = Paginator(posts_list, 5)
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)
	
	context = {
		'queryset': queryset,
		'posts': queryset,
		'categories': categories_list,	
	}
	return render(request, 'main/index.html', context)

def view_aboutpage(request):
	return render(request, 'main/about.html', {})

def custom_404(request):
	response = render_to_response('main/404.html', {}, context_instance=RequestContext(request))
	response.status_code = 404
	return response

def custom_500(request):
	response = render_to_response('main/500.html', {}, context_instance=RequestContext(request))
	response.status_code = 500
	return response

class blog_sitemap(Sitemap):
	changefreq = "daily"
	priority = 1.0
	lastmod = datetime.datetime.now()
	def items(self):
		return Post.objects.all()