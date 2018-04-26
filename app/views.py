from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

import json
import requests
from .models import Githubdata
from django.core import serializers

# Create your views here.
@login_required(login_url='/login/')
def home(request):
    return render(request, 'app/home.html')

def log_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(reverse('app:home'))
        else:
            print(form.errors)
    return render(request, 'app/login.html', {'form': form})

@login_required(login_url='/login/')
def log_out(request):
    logout(request)
    return redirect(reverse('app:login'))

def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('app:login'))
        else:
            print(form.errors)
    return render(request, 'app/signup.html', {'form': form})

@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'app/dashboard.html')


################################### STALK ON GITHUB #######################################

@login_required(login_url='/login/')
def stalk_on_github(request):
    request.session['github'] = True

    username = request.GET.get('filter')
    url = 'https://api.github.com/users/{}/events/public'.format(username)

    try:
        res = requests.get(url).json()
    except:
        return HttpResponse("failed")
    res = json.dumps(res)


    github_data = Githubdata.objects.filter(user=request.user).first()
    if github_data == None:
        print("creating Githubdata model instance")
        # Create a model instance to store victim's github activity
        Githubdata.objects.create(user=request.user, service='github', data=res, victim=username)
    else:
        print("Githubdata model instance already exists")
        # If similar model instance exists, update its data field to the new JSON payload
        github_data.data = res
        github_data.victim = username
        github_data.save()

    return HttpResponse("success")


def github_report(request):
    github = Githubdata.objects.filter(user=request.user).first()
    if github == None:
        return HttpResponse(status=500)
    info = github.data
    string = json.loads(info)

    return JsonResponse(string, safe=False)

def remove_github(request):
    del request.session['github']
    github = Githubdata.objects.filter(user=request.user).delete()
    return HttpResponse("success")


################################### STALK ON FACEBOOK #######################################

@login_required(login_url='/login/')
def stalk_on_facebook(request):
    request.session['facebook'] = True

    username = request.GET.get('filter')
    # url = 'https://api.github.com/users/{}/events/public'.format(username)

    # try:
    #     res = requests.get(url).json()
    # except:
    #     return HttpResponse("failed")
    # res = json.dumps(res)


    facebook_data = Facebookdata.objects.filter(user=request.user).first()
    if facebook_data == None:
        print("creating Facebookdata model instance")
        # Create a model instance to store victim's facebook activity
        Facebookdata.objects.create(user=request.user, service='facebook', data=res, victim=username)
    else:
        print("Facebookdata model instance already exists")
        # If similar model instance exists, update its data field to the new JSON payload
        facebook_data.data = res
        facebook_data.victim = username
        facebook_data.save()

    return HttpResponse("success")

def facebook_report(request):
    facebook = Facebookdata.objects.filter(user=request.user).first()
    if facebook == None:
        return HttpResponse(status=500)
    info = facebook.data
    string = json.loads(info)

    return JsonResponse(string, safe=False)

def remove_facebook(request):
    del request.session['facebook']
    facebook = Githubdata.objects.filter(user=request.user).delete()
    return HttpResponse("success")
