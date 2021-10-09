from django.urls import path

from world.views import CityList, CityDetail, CountryList, CountryDetail

urlpatterns = [
    path('', CityList.as_view(), name='city_list'),
    path('<int:pk>/', CityDetail.as_view(), name='city_detail'),
    path('country/', CountryList.as_view(), name='country_list'),
    path('country/<str:slug>/', CountryDetail.as_view(), name='country_detail'),

]