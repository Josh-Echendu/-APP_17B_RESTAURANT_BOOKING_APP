from django.db import models
from django.contrib.auth.models import User

# User is a  class that represent a database model, i.e the User database model
# User is also a table in a database which contains, the user_name, password as columns

# Drop down list
MEAL_TYPE = (
    ("starters", "Starters"), # This "starters" is used by backend, and "Starters" is used by frontend
    ("salad", "Salads"),
    ("main_dishes", "Main Dishes"),
    ("desserts", "Desserts")
)

# Drop down list
STATUS = (
    (0, "Unavailable"), 
    (1, "Available")
)

# Create your models here.

class Item(models.Model): # item is also a table
    meal = models.CharField(max_length=80, unique=True) # we shouldnt have duplicated meal, that why we used a 'unique' constraints
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # For the meal category
    meal_type = models.CharField(max_length=200, choices=MEAL_TYPE)

    # What happens when a meal is deleted, PROTECT means you wont delete the meal
    author = models.ForeignKey(User, on_delete=models.PROTECT) # We are creating a one to many relationship between the item table and the User table
    # i.e one cook can create many meals, item = meals and User = cook

    status = models.IntegerField(choices=STATUS, default=1) # By default the meal is set to unavailable
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    
    # When the item would be printed out, it woild be represented by meal
    def __str__(self):
        return self.meal

