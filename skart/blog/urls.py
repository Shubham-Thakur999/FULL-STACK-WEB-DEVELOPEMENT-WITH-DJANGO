from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="blogHome"),
    path("blogpost/<int:id>", views.blogpost, name="blogHome")
    #In this tutorial, we will create a Django post page for displaying the blog content. While creating the Blogpost model or table, we defined an object named blog id in the database. Now, we will use this id to display the blog content uniquely. To do so, open the urls.py file of the blog app and type the above code.In the above code, we've passed the blog id in the blogpost function. 
]