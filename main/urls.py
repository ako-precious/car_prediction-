

from django.urls import path
from . import views
 
app_name = "main"

urlpatterns = [
    #path('aa', views.ItemView, name="items"),
    path('', views.PredictionView, name="items"),
   
]

