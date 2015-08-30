from django import forms

class FizzBuzzForm(forms.Form):
    fizzbuzz_number = forms.CharField(label='FizzBuzz number', max_length=100)