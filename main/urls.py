from django.urls import path
from . import views


urlpatterns = [
	path("", views.home, name="home"),
	path("upload/", views.upload, name="upload"),
	path("process_img/", views.process_img, name="process_img")
]

