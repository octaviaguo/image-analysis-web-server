from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
'''
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
	HTTP_200_OK,
	HTTP_400_BAD_REQUEST,
	)
'''
from .models import ImgClassify

path = ''

def home(request):
	return render(request, "main/home.html")

def upload(request):
	context={}
	if request.method == 'POST' and request.FILES['document']:
		upFile = request.FILES['document']
		fstore = FileSystemStorage()
		name = fstore.save(upFile.name, upFile)
		context['url'] = fstore.url(name)
		path =  '..'+ context['url']
	return render(request, "main/upload.html", context)


#@api_view(['POST'])
#@permission_classes((AllowAny,))
def process_img(request):
	global path 
	context = {}
	img_obj = ImgClassify(path)		
	result = img_obj.classify()
	context['result'] = result

	return render(request, "main/classification.html", context)
	

