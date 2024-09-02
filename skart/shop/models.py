from django.db import models

# Create your models here.(here we create all our tables like we do in DBMS.)

class Product(models.Model):
    product_id = models.AutoField
    # above we created a column called "product_id" and we added (AutoField) to it.(AutoField) is an integer data type which increment its length automatically.
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    # below column named "image" will store image of various products.it will upload images to the folder or directory ("shop/images")
    image = models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name
    # above we have defined a method or function to show us the name of the products(like : watch,ipad,etc..) instead of(product.object 1,project.object 2,etc..)


# ABOVE TABLE WILL STORE INFO RELATED TO EACH PRODUCT.
# NOW IF WE WANT TO SEE THIS TABLE IN OUR ADMIN SITE THEN WE MUST ADD THIS (MODEL) TO THE (admin.py) file of this app "shop".

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name


# ABOVE MODEL OR TABLE WILL STORE DATA FROM THE "CONTACT" PAGE.(we have already learned all this while making "Contact Us" page of our (portfolio website)).


def __str__(self):
    return self.product_name
# above we have defined a method or function to show us the name of the products(like : watch,ipad,etc..) instead of(product.object 1,project.object 2,etc..)

class Orders(models.Model):
    order_id= models.AutoField(primary_key=True)
    #above we made the "order_id" column as the primary key of our table or model.obviously each order should be unique only.
    items_json= models.CharField(max_length=5000)
    #upar waale column me har order ki (json) file store hogi.json me kuch nahi bas order details hi hai dictionary{ke:value}pair ke roop me.

    #Before integrating the payment gateways, we need to fetch the total amount in the back-end. So, open the modsels.py file of the shop app and type the below statement.
    amount=models.IntegerField(default=0)
    #In the above code, we've included a new object named amount in the pre-existing model Order.WE'LL NEED IT TO CATCH THE (PRICE) OF PRODUCTS ,WHICH WILL BE USED TO WHILE MAKING Payments on "checkout.html".

    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)
    phone=models.CharField(max_length=111,default="")

# Now, we will create a new model to track the orders. So, get into the shop/models.py file and type the below code :
class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)

def __str__(self):
    return self.update_desc[0:7] + "..."
    #above statement will show first (7 or 8) letters of description  (as we have sliced it through: update_desc[0:7]) 