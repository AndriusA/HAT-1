from django.contrib import admin

from .models import Location, LocationType, LocationThingCrossRef, LocationThingRelationshipType


class LocationAdmin(admin.ModelAdmin):
    pass


class LocationTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Location)
admin.site.register(LocationType)
admin.site.register(LocationThingCrossRef)
admin.site.register(LocationThingRelationshipType)
