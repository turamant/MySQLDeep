from django.contrib import admin

# Register your models here.
from world.models import City, Country, Countrylanguage


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = (id, 'name',
                    'countrycode', 'district',
                    'population')


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'continent', 'region', 'surfacearea', 'indepyear',
                    'population', 'lifeexpectancy', 'gnp', 'gnpold', 'localname',
                    'governmentform', 'headofstate', 'capital', 'code2')


@admin.register(Countrylanguage)
class CountrylanguageAdmin(admin.ModelAdmin):
    list_display = ('countrycode', 'language', 'isofficial', 'percentage')


admin.site.site_title = "Best Prices 🔥🔥"
admin.site.site_header = "Best Prices 🔥🔥"