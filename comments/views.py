from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
# Structural Imports here.
from .models import Comment
from .forms import CommentForm
# Create your views here.
def comment_thread(request, id):
	instance = get_object_or_404(Comment, id=id)
	initial_data = {
		"content_type": instance.content_type,
		"object_id": instance.object_id,
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
	context = {
		'comment': instance,
		'comment_form': form,
	}
	return render(request, "comments/comment_thread.html", context)