from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def home(request):
	return render(request, "main/home.html")

def upload(request):
	context={}
	if request.method == 'POST' and request.FILES['document']:
		upFile = request.FILES['document']
		fstore = FileSystemStorage()
		name = fstore.save(upFile.name, upFile)
		context['url'] = fstore.url(name)
	return render(request, "main/upload.html", context)

