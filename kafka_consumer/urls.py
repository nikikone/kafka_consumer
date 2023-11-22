from django.urls import path
from . import views

urlpatterns = [
    path('api/zones/', views.get_list, name='get'),
]
