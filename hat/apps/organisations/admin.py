from django.contrib import admin

from .models import Organisation, OrganisationAddress, OrganisationContactMethod, OrganisationType


class OrganisationAdmin:
    pass


class OrganisationAddressAdmin:
    pass


class OrganisationMethodAdmin:
    pass


class OrganisationTypeAdmin:
    pass


admin.site.register(Organisation)
admin.site.register(OrganisationAddress)
admin.site.register(OrganisationContactMethod)
admin.site.register(OrganisationType)