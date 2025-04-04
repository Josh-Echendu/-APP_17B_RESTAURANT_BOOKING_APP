from django.shortcuts import render
from django.views import generic
from .models import Item


# List type of page
class MenuList(generic.ListView): # This class is good for displaying pages which have lot of data i.e a list type of page
    
    # Connecting the database model to the view 
    # we are querying the data from the database table, when we add data from the admin
    queryset = Item.objects.order_by("-date_created") # Its a variable that will stores a list of data
    template_name = "index.html"

    # Sending python values to your html codes
    def get_context_data(self): # This is a predifined method, it is a method that is part of the listview class
        context = {"meals": ['pasta', "Pizza"],
                    'ingredients': ['pepper', 'maggi']} # This shows you can send values from python to your html codes
        return context

class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"

# Connected to "indexB.html"    