from django.shortcuts import render,redirect
from django.contrib.contenttypes.models import ContentType
from .models import Comment
from django.urls import reverse
from .forms import CommentForm
from django.http import JsonResponse

def update_comment(request):
    referer = request.META.get('HTTP_REFERER',reverse('home'))
    comment_form = CommentForm(request.POST,user=request.user)
    if comment_form.is_valid():
        comment = Comment()
        comment.user=request.user
        comment.text=comment_form.cleaned_data['text']
        comment.content_object = comment_form.cleaned_data['content_object']
        parent = comment_form.cleaned_data['parent']
        if not parent is None:
            comment.root = parent.root if not parent.root is None else parent
            comment.parent = parent
            comment.reply_to = parent.user

        comment.save()
        data ={}
        data['status']='SUCCESS'
        data['username']=comment.user.get_nickname_or_username()
        data['comment_time'] =comment.comment_time.timestamp()
        data['text']=comment.text
        data['content_type']=ContentType.objects.get_for_model(comment).model
        if not parent is None:
            data['reply_to'] = comment.reply_to.get_nickname_or_username()
        else:
            data['reply_to']=''
        data['pk'] = comment.pk
        data['root_pk']=comment.root.pk if not comment.root is None else ''
    else:
        data={}
        data['status']='ERROR'
        data['message'] = list(comment_form.errors.values())[0]
        #return render(request,'error.html',{'message':comment_form.errors,'redirect_to':referer})
    return JsonResponse(data)
# Create your views here.
