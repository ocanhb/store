from django.urls import path
from . import views

urlpatterns = [
    path('predict/', views.size_predictor, name='size_predictor'),
]

