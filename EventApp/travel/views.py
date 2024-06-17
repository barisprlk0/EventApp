from django.shortcuts import render, redirect, get_object_or_404
from .models import TravelModel,Rating
from .forms import TravelForm,RatingForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def create_view(request):
    if request.method== "POST":
        form= TravelForm(request.POST,request.FILES)
        if form.is_valid():
            travel= form.save(commit=False)
            travel.author=request.user  
            travel.save()
            return redirect('account:profile')
    else:
        form= TravelForm()
    return render(request, 'travel/create_form.html',{'form':form})

def index_view(request):
     events= TravelModel.objects.all()
     return render(request,'travel/index.html',{'events':events})


def detail(request,id):
     post = get_object_or_404(Rating, id=id)
     travel=get_object_or_404(TravelModel,id=id)
     return render(request, 'travel/detail.html',{'travel':travel,'post':post})

def update_view(request, id):
    travel = get_object_or_404(TravelModel, id=id)
    if request.user==travel.author:

        if request.method == "POST":
            form = TravelForm(request.POST, request.FILES, instance=travel)
            if form.is_valid():
                form.save() 
                return redirect('account:profile')
        else:
            form = TravelForm(instance=travel)
    else:
        return redirect('home:index')
    return render(request, 'travel/create_form.html', {'form': form, 'travel': travel})

def delete_view(request,id):
    travel=get_object_or_404(TravelModel,id=id)
    if request.user==travel.author:
        if request.method=="POST":
            travel.delete()
            return redirect('account:profile')
    else:
        return redirect('home:index')
    return render(request, 'travel/delete_confirm.html', {'travel': travel})


@login_required
def rate_post(request,id):
    post= get_object_or_404(TravelModel,id=id)
    if request.method=="POST":
        form=RatingForm(request.POST)
        if form.is_valid():
            rating, created= Rating.objects.update_or_create(
                user=request.user,
                travel_post=post,
                defaults={'value':form.cleaned_data['value']}
            )
            return redirect('home:index') ##değişecek
        
    else:
        form=RatingForm()
    return render(request, 'travel/rate_post.htsml',{'form':form,'post':post})
