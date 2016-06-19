from __future__ import absolute_import

from celery import shared_task

from fizzbuzz.models import FizzBuzzResult


@shared_task
def fizz_buzz(x):
    devided_3 = x % 3 == 0
    devided_5 = x % 5 == 0
    if devided_3 and devided_5:
        result = 'fizzbuzz'
    elif devided_3:
        result = 'fizz'
    elif devided_5:
        result = 'buzz'
    else:
        result = x
    fizz_buzz_result = FizzBuzzResult(fb_input=x, fb_result=result)
    fizz_buzz_result.save()
