from .views import *
from django.urls import path

urlpatterns = [
    path('api/add/', Add.as_view()),
    path('api/get/', Get.as_view()),
]
