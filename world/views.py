from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView

from django.db.models import Count

from world.models import City, Country


def get_city_list(request):
    #cities = City.objects.select_related("countrycode").filter(population__gt=7000000)
    cities = City.objects.select_related("countrycode").all()
    return render(request, 'city/city_list.html', {'cities': cities})

def get_city_detail(request, pk):
    city = get_object_or_404(City, pk=pk)
    return render(request, 'city/city_detail.html', {'city': city})


def get_country_list(request):
    countries = Country.objects.all()
    return render(request, 'country/country_list.html', {'countries': countries})


def get_country_detail(request, slug):
    country = get_object_or_404(Country, code=slug)
    cities = City.objects.select_related('countrycode').filter(countrycode=country.code)
    return render(request, 'country/country_detail.html', {'country': country,
                                                           'cities': cities,
                                                           })




