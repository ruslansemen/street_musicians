from django.urls import path
from .views import index, index_1

urlpatterns = [
    path('', index),
    path('1/', index_1)
]
