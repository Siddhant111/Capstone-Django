from django.shortcuts import render
import os

from django.core.files.storage import FileSystemStorage
from django.conf import settings

# Create your views here.

def diagnostic(request):
    if request.method == 'POST':
        file_path = os.path.join(settings.BASE_DIR, 'models\\research\\object_detection')
        os.system('python ' + file_path + '\\object_detection_tutorial.py')
    return render(request, 'diagnostic.html')
