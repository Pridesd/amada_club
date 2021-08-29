from django.shortcuts import redirect, render, get_object_or_404
from django.http import request
from django.utils import timezone
from .models import Community

def community(request):
    post_list = Community.objects.all().order_by('-id')
    return render(request, 'community.html', {'post_list':post_list})

def co_detail(request, id):
    post = get_object_or_404(Community, pk = id)
    return render(request, 'co_detail.html', {'post':post})

def co_new(request):
    return render(request, 'co_new.html')

def co_create(request):
    new_post = Community()
    new_post.title = request.POST['title']
    new_post.content = request.POST['content']
    new_post.date = timezone.now()
    if (request.FILES.get('image') is not None) :
        new_post.image = request.FILES['image']
    else:
        return render(request, 'co_new.html')
    new_post.save()

    return redirect('co_detail', new_post.id)

def co_edit(request, id):
    post = get_object_or_404(Community, pk = id)
    return render(request, 'co_edit.html', {'post':post})

def co_update(request, id):
    update_post = Community.objects.get(id = id)
    update_post.title = request.POST['title']
    update_post.content = request.POST['content']
    update_post.date = timezone.now()
    if (request.FILES.get('image') is not None) :
        update_post.image = request.FILES['image']
    update_post.save()

    return redirect('co_detail', update_post.id)

def co_delete(request, id):
    delete_post = Community.objects.get(id = id)
    delete_post.delete()
    return redirect('community')
# Create your views here.
