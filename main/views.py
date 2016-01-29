from django.shortcuts import render, render_to_response, get_object_or_404
# Create your views here.

def view_homepage(request):
	return render(request, 'main/index.html', {})

def view_aboutpage(request):
	return render(request, 'main/about.html', {})

def view_contactpage(request):
	return render(request, 'main/contact.html', {})