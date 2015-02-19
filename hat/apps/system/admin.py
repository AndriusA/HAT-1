from django.contrib import admin

from .models import (Currency, UnitOfMeasurement, Nationality, Ethnicity, Gender,
                     MaritalStatus, Religion, Prefix)


class UnitOfMeasurementAdmin(admin.ModelAdmin):
    fields = ('name', 'symbol', 'description', )


class NationalityAdmin(admin.ModelAdmin):
    pass


class EthnicityAdmin(admin.ModelAdmin):
    pass


class GenderAdmin(admin.ModelAdmin):
    pass


class MaritalStatusAdmin(admin.ModelAdmin):
    pass


class ReligionAdmin(admin.ModelAdmin):
    pass


class PrefixAdmin(admin.ModelAdmin):
    pass


admin.site.register(UnitOfMeasurement, UnitOfMeasurementAdmin)
admin.site.register(Nationality)
admin.site.register(Ethnicity)
admin.site.register(Gender)
admin.site.register(Religion)
admin.site.register(Prefix)
