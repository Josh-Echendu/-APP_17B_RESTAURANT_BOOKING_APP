from typing import Any
from django.shortcuts import render
from django.views import generic
from .models import Item, MEAL_TYPE, STATUS

# Create your views here.

# List type of view
# This is used to handle the home page
class MenuList(generic.ListView): # This class is good for displaying pages which have lot of data i.e a list type of page
    queryset = Item.objects.order_by("-date_created") # Its a variable that will stores a list of data
    template_name = "index.html"

    # Sending python values to your html codes
    def get_context_data(self, **kwargs): # 
        context = super().get_context_data(**kwargs) # We are getting an existing dictionary from the list_view class to get some default value, rather than having an empty dictionary

        # Add a key to the dictionary
        context["meals"] = MEAL_TYPE # This shows you can send python values to your html codes
        
        return context

# This is used to handle the other pages on the website
class MenuItemDetail(generic.DetailView):
    
    model = Item # database model
    template_name = "menu_item_detail.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['statuses'] = STATUS

        return context

#connected to 'indexD.html' and 'indexE.html'    