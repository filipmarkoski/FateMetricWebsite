"""fatemetric URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from main.views import blog_sitemap, custom_404, custom_500
from django.http import HttpResponse

from django.shortcuts import render
from django.conf.urls import handler404, handler500

''' Django Rest Framework '''
from blog import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categories', views.CategoriesViewSet)
router.register(r'posts', views.PostViewSet)

sitemaps = {
    'blogs': blog_sitemap
}

urlpatterns = [
    # Django URLs
    path('admin/', admin.site.urls),

    # Third Part URLs
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('favicon.urls')),

    path('robots.txt', lambda r: HttpResponse("User-agent: *\nDisallow:", content_type="text/plain")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    # FateMetric URLs
    path('', include('main.urls')),
    path('blog/', include('blog.urls')),
    path('chat/', include('chat.urls')),

    # include((pattern_list, app_namespace), namespace=None)
    path('comments/', include(('comments.urls', 'comments'),
                              namespace='comments')),
    # url(r'^', include('games.urls')),

    # Apparently, the URLs are read backwards,
    # meaning FateMetric URLs need to be
    # overwritten by rest_framework.urls

    # This URL (router) changes the home page.
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if DEBUG is True it will be served automatically
if settings.DEBUG is False:
    urlpatterns += path(r'^static/(?P<path>.*)$',
                        'django.views.static.serve',
                        {'document_root': settings.STATIC_ROOT})

# Error Handlers


def response_error_handler(request, exception=None):
    # return HttpResponse('Error handler content', status=403)
    # return render(request, 'polls/detail.html', {'question': question})
    return render(request, 'main/404.html')


# handler404 = 'main.views.custom_404'
handler404 = response_error_handler

handler500 = 'main.views.custom_500'
