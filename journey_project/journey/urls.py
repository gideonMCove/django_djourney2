from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('citys/', views.CityList.as_view(), name='city_list'),
    path('city/<int:pk>', views.CityDetail.as_view(), name='city_detail'),
    path('attractions/', views.AttractionsList.as_view(), name='attractions_list'),
    path('attraction/<int:pk>', views.AttractionsDetail.as_view(), name='attractions_detail'),
    path('reviews/', views.ReviewsList.as_view(), name='reviews_list'),
    path('review/<int:pk>', views.ReviewsDetail.as_view(), name='reviews_detail'),
]