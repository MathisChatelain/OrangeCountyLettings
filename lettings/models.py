from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db import models


class Address(models.Model):
    """
    Address model

    uses number and street as representation
    """

    class Meta:
        """
        NOTE : this Model was originially created in the oc_lettings_site app
        and then moved to lettings app since it is related to the Letting model
        """

        db_table = "oc_lettings_site_address"

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    def __str__(self):
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """Letting model"""

    class Meta:
        """
        NOTE : this Model was originially created in the oc_lettings_site app
        """

        db_table = "oc_lettings_site_letting"

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
