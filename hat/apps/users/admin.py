from django.contrib import admin

from .models import (Person, PersonAddress, PersonContactMethod, AffiliateService,
                     Emotion, EmotionType, PersonToPersonRelationshipType)


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


class PersonToPersonRelationshipAdmin(admin.ModelAdmin):
    pass


class EmotionAdmin(admin.ModelAdmin):
    pass


class EmotionTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person)
admin.site.register(PersonToPersonRelationshipType)
admin.site.register(PersonAddress)
admin.site.register(PersonContactMethod)
admin.site.register(AffiliateService)
admin.site.register(Emotion)
admin.site.register(EmotionType)
