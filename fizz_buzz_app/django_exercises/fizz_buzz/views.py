from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import FizzBuzzForm 
from .services import calc_fizz_buzz

# Create your views here.
def fizz_buzz(request):
    if request.method == 'POST':
        form = FizzBuzzForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('fizz_buzz/fizz_buzz_result.html', request)
    else:
        form = FizzBuzzForm()
    return render(request, 'fizz_buzz/fizz_buzz.html', {'form': form})

def fizz_buzz_result(request):
    num = request.POST['fizzbuzz_number']
    result = calc_fizz_buzz(int(num))
    return render(request, 'fizz_buzz/fizz_buzz_result.html', {'fizzbuzz_number': result})
