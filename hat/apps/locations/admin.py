from django.contrib import admin

from .models import Location, LocationType, LocationThingCrossRef


class LocationAdmin(admin.ModelAdmin):
    pass


class LocationTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Location)
admin.site.register(LocationType)
admin.site.register(LocationThingCrossRef)
