from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns=[
    path('register/',RegistrationView.as_view(),name='User_Registration'),
    path('register/<int:pk>/',RegistrationView.as_view(),name='GET-User_Details'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('token/', TokenObtainPairView.as_view(), name='token_access'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('recipe/',RecipeView.as_view(),name='Recipe_data'),
    path('recipe/<int:pk>/',RecipeView.as_view(),name='Recipe_details'),
    path('recipe/<str:category>/', RecipeCategoryView.as_view(),name='Recipe_by_category'),
    path('ratings/', RatingView.as_view(), name='rating-create'),
    path('ratings/<int:pk>/', RatingView.as_view(), name='rating-create'),
    path('recipe/<int:pk>/ratings/', AllRatingRecipe.as_view(), name='recipes all rating'),
    
]