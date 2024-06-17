from django.shortcuts import render, redirect, get_object_or_404
from .forms import AnnouncementForm
from .models import AnnouncementModel
# Create your views here.
def create_view(request):
    if request.method == "POST":
        form= AnnouncementForm(request.POST)
        if form.is_valid():
            post= form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('account:profile')
    else:
        form=AnnouncementForm()
    return render(request,'announcement/create_form.html',{'form':form})
    
def delete_view(request,id):
    post=get_object_or_404(AnnouncementModel,id=id)
    if request.user==post.author:
        if request.method=="POST":
            post.delete()
            return redirect('account:profile')
    else:
        return redirect('account:profile')
    return render(request, 'announcement/delete_form.html', {'post': post})    

def detail_view(request,id):
    post= get_object_or_404(AnnouncementModel, id=id)
    return render(request, 'announcement/detail.html',{'post':post})

def update_view(request,id):
    post=get_object_or_404(AnnouncementModel,id=id)
    if request.user == post.author:
        if request.method=="POST":
            form=AnnouncementForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('account:profile')
        else:
            form = AnnouncementForm(instance=post)

    else:
        return redirect('account:profile')
    
    return render(request,'announcement/create_form.html',{'form':form})