from django.urls import path
from .views import *

app_name = 'crudapp'
urlpatterns = [
    path('',Homepage,name='Home'),
    path('delete/<int:id>',delete,name='delete'),
    path('edit/<int:id>',edit,name='edit'),
]
