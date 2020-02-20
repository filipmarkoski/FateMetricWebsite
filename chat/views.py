from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, Http404
# Structural Imports here.
from chat.models import Chat


# Create your views here.
def view_chat(request):
    messages = Chat.objects.order_by('-timestamp')[:20]
    context = {
        'messages': messages,
    }
    return render(request, 'chat/chat.html', context)


def message(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            message = request.POST.get('message', None)
            message_object = Chat(user=request.user, message=message)
            if message != '':
                message_object.save()
            response_data = {}
            return JsonResponse(response_data)
    else:  # This doesn't work.
        return HttpResponseRedirect('/accounts/login/')

    return 200
