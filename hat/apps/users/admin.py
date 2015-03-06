from django.contrib import admin

from .models import (Person, PersonAddress, PersonContactMethod, AffiliateService,
                     PersonToPersonRelationshipType, PersonAddressLocationCrossRef, Recipient, PersonDataDebitCrossRef, PersonToPersonCrossRef)


class PersonAdmin(admin.ModelAdmin):
    pass


class PersonAddressAdmin(admin.ModelAdmin):
    pass


class OrganisationAdmin(admin.ModelAdmin):
    pass


class OrganisationAddressAdmin(admin.ModelAdmin):
    pass


class OrganisationContactMethodAdmin(admin.ModelAdmin):
    pass


class AffiliateServiceAdmin(admin.ModelAdmin):
    pass


class PersonContactMethodAdmin(admin.ModelAdmin):
    pass


class PersonToPersonCrossRefAdmin(admin.ModelAdmin):
    pass


class PersonToPersonRelationshipTypeAdmin(admin.ModelAdmin):
    pass


class PersonAddressLocationCrossRefAdmin(admin.ModelAdmin):
    pass


class RecipientAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person)
admin.site.register(PersonToPersonRelationshipType)
admin.site.register(PersonAddress)
admin.site.register(PersonContactMethod)
admin.site.register(AffiliateService)
admin.site.register(PersonAddressLocationCrossRef)
admin.site.register(Recipient)
admin.site.register(PersonToPersonCrossRef)
# admin.site.register(Emotion)
# admin.site.register(EmotionType)
# Emotion, EmotionType,
