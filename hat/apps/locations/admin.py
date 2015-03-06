from django.contrib import admin

from .models import LocationToLocationCrossRef, LocationThingRelationshipType, Location, LocationType, LocationThingCrossRef, LocationToLocationRelationshipType, LocationPersonCrossRef, LocationPersonRelationshipType

class LocationAdmin(admin.ModelAdmin):
    pass


class LocationTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Location)
admin.site.register(LocationType)
admin.site.register(LocationThingCrossRef)
admin.site.register(LocationThingRelationshipType)
admin.site.register(LocationToLocationCrossRef)
admin.site.register(LocationToLocationRelationshipType)
# admin.site.register(LocationSensorCrossRef)
# admin.site.register(LocationSensorRelationshipType)
admin.site.register(LocationPersonCrossRef)
admin.site.register(LocationPersonRelationshipType)

# LocationSensorCrossRef, LocationSensorRelationshipType








