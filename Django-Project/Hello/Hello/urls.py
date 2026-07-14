from django.contrib import admin
from django.urls import path
from Hello.Views import My_first_project

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', My_first_project), 
]