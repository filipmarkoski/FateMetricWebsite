from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.sitemaps import Sitemap
from django.contrib import messages
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, Http404
from django.db.models import Q
from blog.models import Post, Categories

from django.utils import timezone
import datetime
# Create your imports here
from blog.forms import CategoriesForm
from comments.models import Comment


# Create your views here.
def view_homepage(request, slug=None):
    categories_list = Categories.objects.all().order_by("id")
    posts_list = Post.objects.active()
    today = timezone.now().date()

    if request.user.is_staff or request.user.is_superuser:
        posts_list = Post.objects.all()

    query = request.GET.get("q")
    if query:
        posts_list = posts_list.filter(
            Q(title__icontains=query) |
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

    categories_form = CategoriesForm(request.POST or None)
    if categories_form.is_valid():
        instance = categories_form.save(commit=False)
        instance.save()
        messages.success(request, "Category Successfully Created")

    comments = Comment.objects.all()
    context = {
        'queryset': queryset,
        'posts': queryset,
        'categories': categories_list,
        'categories_form': categories_form,
        'comments': comments,
    }
    return render(request, 'main/index.html', context)


def view_aboutpage(request):
    return render(request, 'main/about.html', {})


@login_required
def view_dislike(request):
    # AJAX Dislike Button
    if request.user.is_authenticated:
        if request.method == 'POST':
            dislikepostId = request.POST['DislikeId']
            dislikepost = get_object_or_404(Post, id=dislikepostId)
            dislikepost.dislikes += 1
            dislikepost.save()
            response_data = {}
            return JsonResponse(response_data)
    else:
        raise Http404

    return 200


@login_required
def view_like(request):
    # AJAX Like Button
    if request.user.is_authenticated:
        if request.method == 'POST':
            likepostId = request.POST.get('LikeId')
            likepost = get_object_or_404(Post, id=likepostId)
            likepost.likes += 1
            likepost.save()
            response_data = {}
            return JsonResponse(response_data)
    else:
        raise Http404

    return 200


def view_contact(request):
    # AJAX Contact Us
    if request.user.is_authenticated:
        if request.method == 'POST':
            PersonEmail = request.POST.get('PersonEmail_ajax', '')
            PersonMessage = request.POST.get('PersonMessage_ajax', '')
            # print(PersonEmail + " " + PersonMessage + " by " + str(request.user) )

            send_mail(str(request.user) + " - " + PersonEmail, PersonMessage, PersonEmail,
                      ['filip.markoski45@gmail.com'], fail_silently=False)

            response_data = {}
            return JsonResponse(response_data)
    else:
        raise Http404

    return 200


def custom_404(request):
    response = render('main/404.html', {}, context=RequestContext(request))
    response.status_code = 404
    return response


def custom_500(request):
    response = render('main/500.html', {}, context=RequestContext(request))
    response.status_code = 500
    return response


class blog_sitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0
    lastmod = datetime.datetime.now()

    def items(self):
        return Post.objects.all()
