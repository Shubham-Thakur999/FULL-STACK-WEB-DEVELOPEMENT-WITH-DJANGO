from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("productView/<int:myid>", views.productView, name="productView"),
    # see above we gave an id <int:myid> in the path variable of the (productView function) in order to take user to the paricular "product" in tat "productView" page.means the "productView" function in "views.py" page will receive the "id" of the products as its (2nd arguement). 
    path("checkout/", views.checkout, name="Checkout"),
    #below path will take us to the (handlerequest) function in "views.py" page.
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
]