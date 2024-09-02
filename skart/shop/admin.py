from django.contrib import admin

# Register your models here.(means here we add moddels or tables that we want to appear in the admin panel).

from . models import Product,Contact,Orders,OrderUpdate

admin.site.register(Product)

# below we registerd the model or table for contact page.
admin.site.register(Contact)

# below we registerd the (Orders) model or table.
admin.site.register(Orders)

# below we registerd the (Orderupdate) model or table.
admin.site.register(OrderUpdate)