from django.shortcuts import render

from lettings.models import Letting
from profiles.models import Profile


def index(request):
    return render(request, "index.html")


def lettings_index(request):
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/lettings_index.html", context)


def letting(request, letting_id):
    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)


def profiles_index(request):
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/profiles_index.html", context)


def profile(request, username):
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
