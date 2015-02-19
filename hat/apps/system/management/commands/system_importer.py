from django.core.management.base import BaseCommand, CommandError
from ....system.models import Ethnicity, Gender, MaritalStatus, Religion, Currency
import json

class Command(BaseCommand):

    def handle(self, *args, **options):

        # Load ethnicities from json
        ethnicities = json.loads(open('hat/data/ethnicities.json').read())['result']

        # Loop ethnicities and add them to database if they can't be found
        for ethnicity_object in ethnicities:
            ethnicity, created = Ethnicity.objects.get_or_create(name=ethnicity_object['name'])
            if created:
                print u"Ethnicity {} created.".format(ethnicity_object['name'])
            else:
                print u"Ethnicity {} already exists.".format(ethnicity_object['name'])


        # Load genders from json
        genders = json.loads(open('hat/data/genders.json').read())['result']

        # Loop genders and add them to database if they can't be found
        for gender_object in genders:
            gender, created = Gender.objects.get_or_create(name=gender_object['name'])
            if created:
                print u"Gender {} created.".format(gender_object['name'])
            else:
                print u"Gender {} already exists.".format(gender_object['name'])


        # Load marriage types from json
        marriage_types = json.loads(open('hat/data/marriage_types.json').read())['result']

        # Loop marriage types and add them to database if they can't be found
        for marriage_type_object in marriage_types:
            marriage_type, created = MaritalStatus.objects.get_or_create(name=marriage_type_object['name'])
            if created:
                print u"Marriage type {} created.".format(marriage_type_object['name'])
            else:
                print u"Marriage type {} already exists.".format(marriage_type_object['name'])


        # Load religions from json
        religions = json.loads(open('hat/data/religions.json').read())['result']

        # Loop religions and add them to database if they can't be found
        for religion_object in religions:
            religion, created = Religion.objects.get_or_create(name=religion_object['name'])
            if created:
                print u"Religion {} created.".format(religion_object['name'])
            else:
                print u"Religion {} already exists.".format(religion_object['name'])


        # Load currencies from json
        currencies = json.loads(open('hat/data/currencies.json').read())['result']

        # Loop currencies and add them to database if they can't be found
        for currency_object in currencies:
            currency, created = Currency.objects.get_or_create(name=currency_object['name'])
            if created:
                print u"Currency {} created.".format(currency_object['name'])
            else:
                print u"Currency {} already exists.".format(currency_ovbject['name'])

