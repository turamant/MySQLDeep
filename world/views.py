from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from world.models import City, Country


class CityList(ListView):
    model = City
    template_name = 'city/city_list.html'
    queryset = City.objects.filter(countrycode='AFG')

class CityDetail(DetailView):
    model = City
    template_name = 'city/city_detail.html'


class CountryList(ListView):
    model = Country
    template_name = 'country/country_list.html'
    #queryset = Country.objects.filter(code='AFG')


class CountryDetail(DetailView):
    model = Country
    template_name = 'country/country_detail.html'
    slug_field = 'code'

