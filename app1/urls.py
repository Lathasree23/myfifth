from django.urls import path
from app1.views import *
app_name='something'

urlpatterns=[
    path('second/',second,name='second'),
]
