"""skart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# below we import further import 2 things.
from django.conf import settings
from django.conf.urls.static import static
#we need to add the below import statement in order to define any path for our "views.py" file of our skart project.
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #ABOVE PATH STATES THAT IF THERE IS (/admin) in addition to the website's url then it will take us to the admin page(which comes freely created by django).
    path('', views.index,name='Home'),
    #above path will initiate when there is no addition to the website url(sirf url).(as we have seen in earlier cases).this path takes us to (index) function of (views.py) page.the name of this path is 'Home'.(we discussed all this in case of our (shop) app)
    path('shop/', include('shop.urls')),
    #ABOVE PATH STATES THAT IF THERE IS (/shop) in addition to the (website's url) then it will be handled by the (urls.py) function of the (shop) app and it will take us to there only and there the further destination will be given to us.
    path('blog/', include('blog.urls')),
     #ABOVE PATH STATES THAT IF THERE IS (/blog) in addition to the (website's url) then it will be handled by the (urls.py) function of the (blog) app and it will take us to there only and there the further destination will be given to us.
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
