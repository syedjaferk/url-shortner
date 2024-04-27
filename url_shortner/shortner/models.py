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
from shortner.unique_id_generator.gen_twitter_snowflake_id import Snowflake
from shortner.unique_id_generator.to_base_62 import to_base62


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
        """        Generate a short code using Snowflake algorithm and base62 encoding.

        This function generates a short code using the Snowflake algorithm with a worker ID of 10,
        and then encodes the generated ID using base62 encoding.

        Returns:
            str: The generated short code.
        """

        snowflake = Snowflake(worker_id=10)
        val = snowflake.generate_id()
        short_code = to_base62(val)
        return short_code
