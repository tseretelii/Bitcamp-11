from django.urls import path
from calculator.views import *

urlpatterns = [
    path('', add_view),
    path('add/<int:first_num>/<int:second_num>', add_view),
    path('subtract/<int:first_num>/<int:second_num>', subtract_view),
    path('divide/<int:first_num>/<int:second_num>', divide_view),
    path('multiply/<int:first_num>/<int:second_num>', multiply_view),
]