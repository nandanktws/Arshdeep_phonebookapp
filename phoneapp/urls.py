from django.contrib import admin
from django.urls import path,include
from phoneapp.views import index,addcontact,search,updatecontact,delete
urlpatterns = [
    
    path('' , index,name="index"),
    path('addcontact/' , addcontact,name="addcontact"),
   
    path('search/' , search,name="search"),
    path('updatecontact/<int:pk>' , updatecontact,name="updatecontact"),
    path('delete/<int:pk>' , delete,name="delete"),
]