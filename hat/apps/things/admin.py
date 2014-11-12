from django.contrib import admin
from django.conf.urls import patterns, url
from django.shortcuts import render
from django.http import HttpResponse

from .models import (Thing, ThingProperty, ThingType, Sensor, SensorData, SensorDataType,
                     ThingSensorCrossRef, ThingSensorRelationshipType)

from .forms import CSVExportForm

import csv


class ThingAdmin:
    pass


class ThingPropertyAdmin:
    pass


class ThingTypeAdmin:
    pass


class SensorAdmin:
    pass


class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('source_description', 'sensor', 'type', 'unit', 'value', 'date_created')
    list_display_links = ('source_description', 'sensor', 'type', 'unit', 'value', 'date_created')

    def get_urls(self):
        urls = super(SensorDataAdmin, self).get_urls()
        my_urls = patterns(
            '',
            url(r'^export/$', self.admin_site.admin_view(self.export_view), name="sensordata_export"),
        )
        return my_urls + urls


    def export_view(self, request):

        # Define fields for admin
        export_fieldsets = (
            (None, {
                "fields": ("start_date", "end_date", "device",),
            }),
        )

        # Check for add and change permission.
        has_add_permission = self.has_add_permission(request)
        has_change_permission = self.has_change_permission(request)
        if not has_add_permission or not has_change_permission:
            raise PermissionDenied

        # Create form instance
        export_form = self.get_form(
            request,
            form=CSVExportForm
        )

        # Check request method for post
        if request.method == "POST":

            # Get instance of form with post data
            form = export_form(request.POST, request.FILES)

            # If form is valid, build CSV response
            if form.is_valid():

                # Get the data we want
                if form.cleaned_data['device']:
                    sensors = Sensor.objects.filter(thingsensorcrossref__thing__in=[form.cleaned_data['device']])
                else:
                    sensors = Sensor.objects.all()
                data = SensorData.objects.filter(sensor__in=sensors)

                # Set response to CSV with filename
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="data_export.csv"'

                # Open response in writer
                writer = csv.writer(response)

                # Add heading rows to CSCV
                writer.writerow([
                    'Device',
                    'Sensor',
                    'Description',
                    'Type',
                    'Unit',
                    'Value',
                    'Date'
                ])

                # Loop the data and add the rows
                for item in data:
                    writer.writerow([
                        item.thing(),
                        item.sensor,
                        item.source_description,
                        item.type,
                        item.unit,
                        item.value,
                        item.date_created
                    ])

                return response

        else:
            form = export_form()


        # Create the admin form.
        admin_form = admin.helpers.AdminForm(form, export_fieldsets, {})

        # Render the template
        media = self.media + admin_form.media

        return render(
            request,
            "admin/things/sensordata/export_form.html", {
                "title": "Export",
                "form": form,
                "adminform": admin_form,
                "opts": self.model._meta,
                "add": False,
                "change": False,
                "is_popup": False,
                "save_as": True,
                "has_add_permission": has_add_permission,
                "has_change_permission": False,
                "has_delete_permission": self.has_delete_permission(request),
                "show_delete": False,
                "has_file_field": False,
                "media": media
            }
        )


class SensorDataTypeAdmin:
    pass


admin.site.register(Thing)
admin.site.register(ThingProperty)
admin.site.register(ThingType)
admin.site.register(Sensor)
admin.site.register(SensorData, SensorDataAdmin)
admin.site.register(SensorDataType)
admin.site.register(ThingSensorCrossRef)
admin.site.register(ThingSensorRelationshipType)
