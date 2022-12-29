from django.urls import path
from app2.views import *
app_name='everything'

urlpatterns=[
    path('third/',third,name='third'),
]