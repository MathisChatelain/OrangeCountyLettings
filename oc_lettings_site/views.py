from django.shortcuts import render

from lettings.models import Letting
from profiles.models import Profile
from django.shortcuts import render


def index(request):
    """Home page, index view"""

    return render(request, "index.html")


def lettings_index(request):
    """Lettings index view, list all lettings"""

    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/lettings_index.html", context)


def letting(request, letting_id):
    """Letting view, show a letting details"""

    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)


def profiles_index(request):
    """Profiles index view, list all profiles"""

    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/profiles_index.html", context)


def profile(request, username):
    """Profile view, show a profile details"""

    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)


def custom_404_view(request):
    """Custom 404 view"""

    return render(request, "errors/404.html", status=404)


def custom_500_view(request):
    """Custom 500 view"""

    return render(request, "errors/500.html", status=500)
