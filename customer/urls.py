from django.contrib import admin
from django.urls import path
from .views import first,Update,Delete,Create

urlpatterns = [
    path('index/',first,name='first'),
    path('ind/<int:uq>',Update,name='update'),
    path('del/<int:uq>',Delete,name='delete'),
    path('cre/',Create,name='create')
    
    
]