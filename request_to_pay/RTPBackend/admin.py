from django.contrib import admin
from django.db.models.base import ModelBase
from . import models
from userapi import models as user_models
# Register your models here.


admin.site.register(user_models.User)
admin.site.register(user_models.UserProfile)

# Custom admin widgets
def makeTabular(model):
    """
    Use Python metaprogramming to
    automatically generate inline forms
    for one-to-many relationships.
    """
    name = model.__name__
    return type(
        f'{name}Inline',
        (admin.TabularInline,),
        dict(
            model=model
        )
    )

class InvoiceAdmin(admin.ModelAdmin):
    inlines = [
        makeTabular(models.Order),
    ]

    def get_changeform_initial_data(self, request):
        return {
            'status': 'A',
            'driver': user_models.UserProfile.objects.filter(user_type='D'),
            'customer': user_models.UserProfile.objects.filter(user_type='B')
            }

class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']



admin.site.register(models.Invoice, InvoiceAdmin)
admin.site.register(models.Item, ItemAdmin)

# Programmatically register every model defined in RTPBackend.models.
# If the model has a custom admin panel, ignore it.
for model in models.__dict__.values():
    if isinstance(model, ModelBase):
        try:
            admin.site.register(model)
        except admin.sites.AlreadyRegistered:
            pass
