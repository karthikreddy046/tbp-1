# crop_prices_app/admin.py
from django.contrib import admin
from .models import Crop, Price
from .models import blog

admin.site.register(blog)
admin.site.register(Crop)
admin.site.register(Price)
