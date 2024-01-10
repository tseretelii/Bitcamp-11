from django.urls import path
from myapp.views import *

urlpatterns = [
    path('', index),
    path('about/', about),
    path('contact/', contact, name='contact'),
    path('success/', success, name='success'),
    path('mad_lib/', your_view_function, name='mad_lib'),
]