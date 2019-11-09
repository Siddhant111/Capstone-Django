from django.shortcuts import render

# Create your views here.

def preventative(request):
    return render(request, 'preventative.html')
