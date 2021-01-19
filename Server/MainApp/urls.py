from .views import Add, Get
from . import views
from django.urls import path

app_name = "MainApp"
urlpatterns = [
    path('api/add/', Add.as_view()),
    path('api/get/', Get.as_view()),
]   