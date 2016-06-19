from django.shortcuts import render, redirect

from fizzbuzz.models import FizzBuzzResult
from fizzbuzz.tasks import fizz_buzz


def home(request, fb=None):
    if request.POST:
        return redirect('fizzbuzz', fb=request.POST['fizzbuzz'])
    fb_result = None
    if fb:
        fb_result = FizzBuzzResult.objects.filter(fb_input=fb)
        if len(fb_result) == 0:
            task_kwargs = dict(x=int(fb))
            fb_result = None
            fizz_buzz.apply_async(kwargs=task_kwargs)
        if fb_result:
            fb_result = fb_result.first().fb_result

        #import ipdb
        #ipdb.set_trace()
    return render(request,
                  'fizzbuzz/home.html',
                  context={'fb_input': fb, 'fb_result': fb_result})
