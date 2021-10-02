# from rest_framework import routers

from django.urls import path

from .views import images_list,images_list_description

urlpatterns = [
    path('image/', images_list),
    path('imagedescription/', images_list_description)
    
    

]