from django.shortcuts import render
from .models import *
from . serializers import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
class RegistrationView(APIView):
    def post(self,request):
        serializer=RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Registration Successfull..!!",status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(slef,rquest,pk=None):
        if pk:
            user=Registration.objects.get(pk=pk)
            serializer=RegistrationSerializer(user)   
            return Response(serializer.data,status=status.HTTP_200_OK)   
        else:
            user=Registration.objects.all()
            serializer=RegistrationSerializer(user,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)


class LoginView(APIView):
    def post(self,request):
        email=request.data.get('email')
        password=request.data.get('password')

        if not email or not password:
            return Response("Email and Password are required", status=status.HTTP_400_BAD_REQUEST)
        try:
            user = Registration.objects.get(email=email)
        except Registration.DoesNotExist:
            return Response("User not registered", status=status.HTTP_404_NOT_FOUND)

        if user.password == password:
            return Response("Login Successful", status=status.HTTP_200_OK)
        else:
            return Response("Invalid Email or Password", status=status.HTTP_401_UNAUTHORIZED)
        

class LogoutView(APIView):
    def post(self,request):
        email=request.data.get('email')
        refresh_token=request.data.get('refresh_token')

        if not email or not refresh_token:
            return Response("Email and refresh token are required.", status=status.HTTP_400_BAD_REQUEST)
        try:
            user=Registration.objects.get(email=email)
        except:
            return Response("User not found.", status=status.HTTP_404_NOT_FOUND)
        token=RefreshToken(refresh_token)
        token.blacklist()
        return Response("Logout Successfully..!!")



class RecipeView(APIView):
    def post(self,request):
        serializer=RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Recipe added Successfully...!!",status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def get(slef,rquest,pk=None):
        if pk:
            try:
                user=Recipe.objects.get(pk=pk)
            except:
                return Response("Recipe not found",status=status.HTTP_404_NOT_FOUND)
            serializer=RecipeSerializer(user)   
            return Response(serializer.data,status=status.HTTP_200_OK)   
        else:
            user=Recipe.objects.all()
            serializer=RecipeSerializer(user,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        

    def put(self,request,pk=None):
        try:
            recipe = Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = RecipeSerializer(recipe, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self,request,pk=None):
        try:
            recipe = Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            return Response("Recipe Not found.", status=status.HTTP_404_NOT_FOUND)
        recipe.delete()
        return Response("Recipe delete successfully.", status=status.HTTP_204_NO_CONTENT)


class RecipeCategoryView(APIView):
    def get(self,request,category):
        if category not in ['breakfast','lunch','dinner']:
            return Response("Invalid category",status=status.HTTP_400_BAD_REQUEST)
        recipe=Recipe.objects.filter(category=category)
        serializer=RecipeSerializer(recipe,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RatingView(APIView):
    def post(self, request):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def get (self,request,pk=None):
        if pk:
            try:
                rating=Rating.objects.get(pk=pk)
            except:
                return Response("Rating not found",status=status.HTTP_404_NOT_FOUND)
            serializer=RatingSerializer(rating)   
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            rating=Rating.objects.all()
            serializer=RatingSerializer(rating,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)


    def delete(self,request,pk=None):
        try:
            rating = Rating.objects.get(pk=pk)
        except Rating.DoesNotExist:
            return Response("Rating Not found.", status=status.HTTP_404_NOT_FOUND)
        rating.delete()
        return Response("Rating delete successfully.", status=status.HTTP_204_NO_CONTENT)


class AllRatingRecipe(APIView):
    def get(self,request,pk=None):
        if pk:
            recipe=Recipe.objects.get(pk=pk)
            rating=Rating.objects.filter(recipe=recipe)
            serializer=RatingSerializer(rating,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response("Recipe Id is Required",status=status.HTTP_400_BAD_REQUEST)