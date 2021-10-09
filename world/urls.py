from django.urls import path

from world.views import get_city_list, get_city_detail, get_country_list, get_country_detail

urlpatterns = [
    #path('', CityList.as_view(), name='city_list'),
    path('', get_city_list, name='city_list'),
    #path('<int:pk>/', CityDetail.as_view(), name='city_detail'),
    path('<int:pk>/', get_city_detail, name='city_detail'),
    #path('country/', CountryList.as_view(), name='country_list'),
    path('country/', get_country_list, name='country_list'),
    #path('country/<str:slug>/', CountryDetail.as_view(), name='country_detail'),
    path('country/<str:slug>/', get_country_detail, name='country_detail'),

]