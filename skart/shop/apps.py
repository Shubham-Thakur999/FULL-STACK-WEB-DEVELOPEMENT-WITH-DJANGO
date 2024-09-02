from django.apps import AppConfig


class ShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop'

# SEE THIS IS THE (APPS.PY) PAGE OF THIS APP (SHOP) AND ABOVE A CLASS CALLED 'ShopConfig' IS ALREADY CREATED FOR US.WE NEED TO JUST COPY THIS CLASS IN (INSTALLED APPS) LIST IN (settings.py) page of project (skart).
