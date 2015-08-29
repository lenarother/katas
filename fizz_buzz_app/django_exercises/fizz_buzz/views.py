from django.shortcuts import render

# Create your views here.
def fizz_buzz(request):
	return render(request, 'fizz_buzz/fizz_buzz.html')