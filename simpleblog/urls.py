from django.urls import path
from simpleblog.views import *

urlpatterns = [
    path('', index)
]