from django.contrib import admin # import the admin module
from .models import Product, User, Cart # import the models from the models.py file
# then we will will register the models to our Admin Site
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Cart)