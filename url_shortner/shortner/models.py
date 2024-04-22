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
        return f"{self.url} | {self.created_at}"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.referenceId = self.generate_short_code()
            self.expires_at = timezone.now() + timedelta(days=30)
        return super().save(*args, **kwargs)

    def generate_short_code(self):
        characters = string.ascii_letters + string.digits
        short_code = ''.join(random.choice(characters) for _ in range(8))
        return short_code
