from django.shortcuts import render
from .models import UploadedFile
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os

@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        file = request.FILES['file']
        file_instance = UploadedFile(file=file)
        file_instance.save()
        return HttpResponse('File uploaded successfully')
    return HttpResponse('Invalid request method')