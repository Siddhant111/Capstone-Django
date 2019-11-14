from django.shortcuts import render

# Create your views here.

def insurance(request):
    return render(request, 'insurance.html')
