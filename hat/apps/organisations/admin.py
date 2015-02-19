from django.contrib import admin

from .models import Organisation, OrganisationAddress, OrganisationContactMethod


class OrganisationAdmin:
    pass


class OrganisationAddressAdmin:
    pass


class OrganisationMethodAdmin:
    pass


admin.site.register(Organisation)
admin.site.register(OrganisationAddress)
admin.site.register(OrganisationContactMethod)
