from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Subscriber)


#REgistration of a model such that the model displays tabular data and n number of fields in the Admin Database by calling admin.ModelAdmin
# @admin.register(Contact) # This could be used and the below deleted
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "subject", "message"]

admin.site.register(Contact, ContactAdmin) # This could be used and the above deleted





