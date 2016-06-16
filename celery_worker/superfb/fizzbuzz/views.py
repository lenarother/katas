from django.shortcuts import render, redirect

# Create your views here.
def home(request, fb=None):
    if request.POST:
        return redirect('fizzbuzz', fb=request.POST['fizzbuzz'])
    return render(request, 'fizzbuzz/home.html', context={'fb': fb})