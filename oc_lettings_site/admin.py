from django.contrib import admin

from lettings.models import Address, Letting
from profiles.models import Profile

admin.site.register(Letting)
admin.site.register(Address)
admin.site.register(Profile)
