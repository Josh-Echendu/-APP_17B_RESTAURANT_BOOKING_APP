from django.shortcuts import render
from django.views import generic
from .models import Item

# List type of page
class MenuList(generic.ListView): # 'ListView', class is good for displaying pages which have lot of data i.e a list type of page
    
    # Connecting the database model to the view 
    # we are querying the data from the database table, when we add data from the admin
    queryset = Item.objects.order_by("-date_created") # Its a variable that will stores a list of data
    template_name = "index.html"

# For a normal type of page
class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"

# The purpose of a view is to get data fro the database model and display those data on the webpage     


# Creating class based views