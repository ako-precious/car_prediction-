

from django.db.models import fields
from rest_framework import serializers
from .models import Item,CarModel
 
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Item
        fields = ("__all__")


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = CarModel
        fields = ("__all__")