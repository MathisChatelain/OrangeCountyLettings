from django.contrib.auth.models import User
from django.db import models

from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    """
    Profile model
    associated with a User model instance

    NOTE : this Model was originially created in the oc_lettings_site app
    and then moved to its own "profiles" app
    """

    class Meta:
        db_table = "oc_lettings_site_profile"
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
