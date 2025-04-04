from django.contrib import admin
from .models import Item

# Register your models here.
class MenuItemAdmin(admin.ModelAdmin):

    # To display the meal and status 
    list_display = ("meal", "status")

    # To display the filter bar, so we can filter our data through status
    list_filter = ("status", )

    # To display the search bar ,  so we could search our data based on meal or description
    search_fields = ("meal", "description")


# Connecting the database to the admin
admin.site.register(Item, MenuItemAdmin)    


# You can add multiple users i.e for the cooks who can add meals on the website
#by using the createsuper 