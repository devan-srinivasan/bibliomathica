from wsgiref.util import request_uri
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.models import Collection
from bibliomath.models import Resource
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.views.generic import ListView

# Create your views here.
def register(request):
    if request.method == 'POST':   
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully create! You can now login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

#decorator allows us to restrict access to the profile page when not logged in
@login_required
def profile(request):
    if request.method == 'POST':   
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)


def collection(request):
    
    collection = Collection.objects.filter(user=request.user)
    collection_res = collection.values('resources')
    resources = []
    for res in collection_res:
        if Resource.objects.filter(id=res['resources']).first() is not None:
            resources.extend(Resource.objects.filter(id=res['resources']))


    context = {
        'collection': collection,
        'resources': resources,
    }
    return render(request, 'users/collection.html', context)


def removeResource(request, id):
    resources = Collection.objects.filter(user=request.user).values('resources')
    
    collection = Collection.objects.filter(user=request.user).first()

    for i in resources:
        if i['resources'] == id:
            r1 = Resource.objects.filter(id=id).first()

    collection.resources.remove(r1)
    collection.save()

    return redirect('collection')
