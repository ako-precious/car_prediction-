

from django.urls import path
from . import views
 
app_name = "main"

urlpatterns = [
    path('', views.ItemView, name="items"),
    path('predict', views.PredictionView, name="items"),
   
]

