from django.contrib import admin

from .models import Event, EventType, EventSensorDataCrossRef, EventSensorDataRelationshipType, DataDebitEventRelationshipType, DataDebitEventCrossRef, DataDebit, DataDebitRecipientCrossRef, EventToEventCrossRef, EventToEventRelationshipType, EventPersonCrossRef, EventPersonRelationshipType
# Register your models here.


class EventAdmin(admin.ModelAdmin):
    pass


class EventTypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Event, EventAdmin)
admin.site.register(EventType, EventTypeAdmin)
admin.site.register(EventSensorDataCrossRef)
admin.site.register(DataDebitEventCrossRef)
admin.site.register(DataDebit)
admin.site.register(DataDebitRecipientCrossRef)
admin.site.register(EventToEventCrossRef)
admin.site.register(EventPersonCrossRef)