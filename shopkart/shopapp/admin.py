from django.contrib import admin
#from .models import Category
#from .models import Product
from .models import *

"""class CategoryAdmin(admin.ModelAdmin):
    list_display=('name', 'image','description')
admin.site.register(Category,CategoryAdmin)"""

admin.site.register(Catagory)
admin.site.register(Product)    

