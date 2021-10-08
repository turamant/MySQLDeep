from django.db import models

# Create your models here.
from django.db.models import Model


class Country(Model):
    ASIA = 'As'
    EUROPE = 'Eu'
    NORTH_AMERICA = 'NA'
    AFRICA = 'Af'
    OCEANIA = 'Oc'
    ANTARCTICA = 'An'
    SOUTH_AMERICA = 'SA'
    CONTINENT = (
        (ASIA, 'Asia'),
        (EUROPE, 'Europe'),
        (NORTH_AMERICA, 'North America'),
        (AFRICA, 'Africa'),
        (OCEANIA, 'Oceania'),
        (ANTARCTICA, 'Antarctica'),
        (SOUTH_AMERICA, 'South America'),
    )
    code = models.CharField(primary_key='Code', max_length=3, null=False, default='')
    name = models.CharField(max_length=52, null=False, default='')
    continent = models.CharField(choices=CONTINENT, null=False, default=ASIA)
    region = models.CharField(max_length=26, null=False, default='')
    surface_area = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    indepyear = models.SmallIntegerField(max_length=6, default=0)
    population = models.IntegerField(max_length=11, null=False, default=0)
    lifeexpectancy = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    gnp = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    gnpold = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    localname = models.CharField(max_length=45, null=False, default='')
    governmentform = models.CharField(max_length=45, null=False, default='')
    headofstate = models.CharField(max_length=60, default='')
    capital = models.IntegerField(max_length=11, default=0)
    code2 = models.CharField(max_length=2, null=False, default='')


class CountryLanguage(Model):
    ISOFFICIAL = ('T', 'F')
    countrycode = models.CharField(max_length=3, null=False, default='')
    language = models.CharField(max_length=30, null=False, default='')
    isofficial = models.CharField(choices=ISOFFICIAL, null=False, default='F')
    percentage = models.DecimalField(max_digits=4, decimal_places=1, null=False, default=0.0)

    class Meta:
        unique_together = ('countrycode', 'language')


KEY
`CountryCode`(`CountryCode`),
CONSTRAINT
`countryLanguage_ibfk_1`
FOREIGN
KEY(`CountryCode`)
REFERENCES
`country`(`Code`)
) ENGINE = InnoDB
DEFAULT
CHARSET = utf8mb4


class City(Model):
    name = models.CharField(max_length=35, null=False, default='')
    countrycode = models.CharField(max_length=3, null=False, default='')
    district = models.CharField(max_length=20, null=False, default='')
    population = models.IntegerField(max_length=11, null=False, default=0)

    PRIMARY
    KEY(`ID`), KEY
    `CountryCode`(`CountryCode`),


CONSTRAINT
`city_ibfk_1`
FOREIGN
KEY(`CountryCode`)
REFERENCES
`country`(`Code`)
) ENGINE = InnoDB
AUTO_INCREMENT = 4082
DEFAULT
CHARSET = utf8mb4
