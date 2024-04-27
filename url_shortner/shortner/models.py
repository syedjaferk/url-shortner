"""
Models for ShortUrls
"""
import uuid
import pytz
import string
import random
from datetime import datetime, timedelta
from django.utils import timezone
from django.db import models


class ShortUrls(models.Model):
    """
    Fields required for short urls
    """
    url = models.URLField(max_length=300)
    referenceId = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def __str__(self):
        """        Return a string representation of the object.

        Returns:
            str: A string containing the URL and creation date of the object.
        """

        return f"{self.url} | {self.created_at}"

    def save(self, *args, **kwargs):
        """        Save the object and generate a reference ID if it's a new instance.

        If the object is new, it generates a short code as a reference ID and sets the expiration date
        to 30 days from the current date.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """

        if not self.pk:
            self.referenceId = self.generate_short_code()
            self.expires_at = timezone.now() + timedelta(days=30)
        return super().save(*args, **kwargs)

    def generate_short_code(self):
        """        Generate a short code consisting of alphanumeric characters.

        This function generates a random short code of length 8 using alphanumeric characters.

        Returns:
            str: A randomly generated short code.
        """

        characters = string.ascii_letters + string.digits
        short_code = ''.join(random.choice(characters) for _ in range(8))
        return short_code
