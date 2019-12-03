from django.contrib import admin
from django.db.models.base import ModelBase
from . import models
from userapi import models as user_models
# Admin site setup
admin.site.site_header = 'Coca-Cola Admin'


# Register your models here.


admin.site.register(user_models.User)

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
    list_display = ['id', 'total_price', 'customer', 'driver']
    list_display_links = ['id', 'customer', 'driver']

    inlines = [
        makeTabular(models.Order),
    ]

    def total_price(self, obj):
        return "${:.2f}".format(obj.price)

    def get_changeform_initial_data(self, request):
        return {'status': 'A', }


class ItemAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'price']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['item', 'price', 'invoice']
    list_display_links = ['item', 'invoice']

    def item(self, obj):
        name = str(obj)
        return name[:name.index('@')]

    def price(self, obj):
        return f"${obj.price}"


admin.site.register(models.Invoice, InvoiceAdmin)
admin.site.register(models.Item, ItemAdmin)
admin.site.register(models.Order, OrderAdmin)

# Programmatically register every model defined in RTPBackend.models.
# If the model has a custom admin panel, ignore it.
for model in models.__dict__.values():
    if isinstance(model, ModelBase):
        try:
            admin.site.register(model)
        except admin.sites.AlreadyRegistered:
            pass
