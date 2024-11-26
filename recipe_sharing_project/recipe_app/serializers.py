from rest_framework import serializers
from .models import *


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Registration
        fields="__all__"

    def validate(self,data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Password and Confirm Password Doest not match")
        return data
        

class RecipeSerializer(serializers.ModelSerializer):
    registraion=RegistrationSerializer(read_only=True)
    class Meta:
        model=Recipe
        fields="__all__"


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'recipe','registration', 'rating', 'review']



