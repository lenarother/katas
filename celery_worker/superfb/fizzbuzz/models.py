from django.db import models


class FizzBuzzResult(models.Model):
    fb_input = models.IntegerField(null=False, blank=False, unique=True)
    fb_result = models.CharField(max_length=30, null=False, blank=False)
