from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('ds/<slug:id>', ids),
    path('ad/', cated),

]