from django.shortcuts import render
from django.http import HttpResponse
# below we import the table or model "Product" which we have created in the "models.py" of "shop" app.the table consisits of various products and thier deatails incliding thier image.(this we'll use in the (index) function below for showong them on homepage or "index.html" )
from .models import Product,Contact,Orders,OrderUpdate
# above imports are also necessary.
from math import ceil
import json
#above we import json module to use it in the code below.JSON  (JavaScript Object Notation) is a file that is mainly used to store and transfer data mostly between a server and a web application. It is popularly used for representing structured data.Python provides a module called json which comes with Python’s standard built-in utility.Note: In Python, JSON data is usually represented as a string.

#the (decorators)are which changes the functionality of a function.as we know the (crsf) token prevents any cross (post request) from any other source,like when you give details to paytm [to take money from this user and send it to my merchant id.then paytm will get all details and will take money from user after verifying everything but it won't be able TO SEND OUR WEBSITE ANY "POST"  REQUEST THAT THE THE PAYMENT HAS BEEN MADE. THIS IS BECAUSE OF (CRSF) TOKEN.SO TO RESTRICT IT FUNCTIONALITY ONLY IN SOME PARTICULAR PART WE IMPORT THE BELOW MWTHOD.
from django.views.decorators.csrf import csrf_exempt
#below has been imported to generate checksum.
from PayTm import Checksum
# Create your views here.
# ???????? the problem is here in this below key's length.
MERCHANT_KEY = 'Your-Merchant-Key-Here'  #  #WorldP64425807474247


# Create your views here.

def index(request):
    products = Product.objects.all()
    # above we store the list of all the products stored in table or model (Product) in a variable called "products".this we do with the help of statement (Product.objects.all()) which we have already seen in (shell) of (terminal).
    #print(products)
    # the above prints all the products.(which we can only see in the terminal.)
    #n= len(products)
    # (n) is the length of [list] called "products"(products list stores a list of products which is 7 in this case as we have stored 7 products. )

    # BELOW FORMULA IS JUST SIMPLE DIVISION PROBLEM THAT YOU TEACH TO STD 3RD KIDS. MEANS IF YOU HAVE 100 PRODUCTS(i.e, n=100) THEN HOW MANY [GROUPS OF 4 CARDS(AS there has to be 4 cards in a single slide)] YOU CAN MAKE.SO WE SIMPLY [DIVIDE 100 BY 4]AND GET (25) AS THE ANSWER,SO THERE WILL BE 25 SLIDES HAVING 4 CARDS EACH INSIDE THEM.
    #nSlides= n//4 + ceil((n/4) - (n//4))
    # SEE THE ABOVE FORMULA WILL GIVE THE (NUMBER OF SLIDES(or GROUP of 4 cards) THAT WE NEED TO SHOW).that is if we have 100 products then what no. of slides will be there? and if there are only 10 products then how many slides we need? . MEANING : see like we have entered 7 products in the database table so the value of n=7. and the FORMULA ABOVE WILL  RETURN THE REQUIRED NUMBER OF SLIDES HAVING 4 CARDS OR PRODUCTS EACH.AS WE DON'T KNOW WHAT NUMBER OF PRODUCTS WILL BE ADDED TO THE DATABASE IN FUTURE SO WE CANNOT DECIDE THE TOTAL NO. OF SLIDES TO SHOW IN THE WEBSITE.so this method helps us in this way.[EX: for n=7 ,nSlides = 7//4 + ceil((7/4) - (7//4)) = 1 + ceil(1.75 - 1) = 1 + ceil(0.75 = 1+1 =2)]{calculated all these calues from python console in pycharm}.SO IN CASE OF 7 PRODUCTS WE'LL NEED 2 SLIDES. [SEE HARRY'S VIDEO ON THIS LOGIC,HE HAS WELL EXPLAINED THIS THING.]

    # *********** PAST FORM OF CODE NO LONGER IN USE**                                                                                        params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    # above we have defined a dictionary named "params" which will return ([value] of some {keys}(as dictionary consists of 'key':value pairs,here the key is some constant like: "no_of_slides","range",etc., and the value is calculated by some given formula)).like the value of constant or key "no_of_slides" is given by formula:n//4 + ceil((n/4) + (n//4)),where n is the length of [list] called "products"(products list stores a list of products which is 7 in this case as we have stored 7 products. )
    # ALSO WE WILL SEND THESE VALUES TO THE (INDEX.HTML) DIRECTLY FROM HERE BY RETURNING THIS DICTIONARY (params) AS AN {ARGUEMENT} IN THE BELOW (RETURN STATEMENT). THIS DICTIONARY WILL RETURN 2(as the value of first variable "nSlides" is used in second variable or key 'range'.) THINGS [1ST IS THE VALUE OF KEY OR CONSTANT named 'range'(which is nothing but a range from 1 to the number of cards or slides stored in the database(as discussed above))]. AND 2ND  IS THE VALUE OF KEY OR CONSTANT CALLED 'product' which is JUST THE [LIST] OF PRODUCTS STORED IN THE DATABASE(alredy explained above).
    # *****************************

    #  ******************** OLD CODE NO. 2**************************************************************                                   allProds=[[products, range(1, len(products)), nSlides],[products, range(1, len(products)), nSlides]]
    # #NOW THE ABOVE COMMENTED CODE WAS GOOD FOR A SINGLE CONTAINER OF SLIDES WHICH GENERALLY REPRESENT'S A SINGLE SEGMENT OF PRODUCTS LIKE THE "MEN'S CLOTHING" CONTAINER WILL HAVE ALL THE SLIDES OF MEN'S CLOTHES.NOW TO ADD OTHER PRODUCT SEGMENTS LIKE "ELECTRONICS" AND "HOME APPLIANCES" WE JUST MODIFY THE PREVIOUS CODE. SEE IN PREVIOUS CODE WE SENT A SINGLE (params) dictionary having values ({'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}) for just 1 CONTAINER OF SLIDES. NOW WE CREATE A [LIST] OF THESE VALUES(i.e, of [nSlides,range(1,nSlides),products]) INSTEAD OF (PARAMS) DICTIONARY HAVING THESE ITEMS AS KEY-VALUE PAIRS. THIS WILL HELP US SEND DATA FOR MULTIPLE {CONTAINER OF SLIDES} THROUGH A SINGLE DICTIONARY NAMRD "params" DEFINED BELOW.  
    # params={'allProds':allProds }
    # # THE ABOVE DICTIONARY NOW HAS CONTENT OR INFORMATION FOR MULTIPLE CONTAINER OF SLIDES AND WE SEND IT TO THE (index.html) file BY GIVING IT AS AN ARGUEMENT IN THE BELOW (RETURN) STATEMENT. 
    # **************************************************************************************************************************************
    allProds = []
    # above is an empty list.
    catprods = Product.objects.values('category', 'id')
    # similar to old codes where we used to store all the products in the above variable, here we are storing the "category" and "id" of all products in the above variable.
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        #above we apply filter() function and place products with same "category" in a variable "prod",which we'll append() or add in the new "allprods" variable along with the length(n) of this variable "prod" and [the no. of slides we can make from it(nSlides)] by the below given statement.
        n = len(prod)
        #as discussed above this above variable will store the length of "prod" variable,which simply tells us about the [no. of products of same(same as we have added similar category products in this variable using filter() function in previous case) category inside it.]
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        #above will calculate the no. of slides we can make from the similar category products.

        #AND FINALLY WE MAKE A LIST OF ALL 3 VALUES CALCULATED ABOVE AND append() or ADD TO THE VARIABLE (allprods).IN THIS MANNER WE'LL BE ABLE TO CREATE SEPRATE [CONTAINER OF SLIDES] FOR EACH CATEGORY OF ITEMS OR PRODUCTS.
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds':allProds}
    #AND WE SEND THE (allprods) variable inside a dictionary (params) to the (index.html) page with the help of below return statement.
    return render(request,"shop/index.html", params)

#below we create a (search) function and we'll implement it with similar logic which we have used in our (index) function(see above).so,that;s why we coopied some of the code from (index) function here directly.

def searchMatch(query, item):
    #This function will return true if the user's query matches the product name or product description; otherwise, it will return false. 
    if query in item.product_name or query in item.category:
        #above if checks if the (item to be searched) is mentioned or present in any of the product's (name)(product_name) or its (category). 
        return True
    else:
        return False

def search(request):
    #below we create a variable named (query) and it'll store the (name or thing) searched by thec user in SearchBar. AUR BHAI YEH BHI CHECK KAR LENA KI TUMNE JAHA BHI SEARCHBAR LAGAYA HO USS (SEARCH ELEMENT) KE CODE ME (method='get' action='/shop/search/') HO TAAKI YAHA TAK, USNE JO BHI SEARCHBOX ME DAALA ENTER KIYA THA AA SAKE.
    query= request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod=[item for item in prodtemp if searchMatch(query, item)]
        #the above conditinal statement checks if the (thing searched by the user) is present in our (list of products or not).and if there are products they will be stored in the (prod) variable and if not nothing will be stored in it .
        n = len(prod)
        # as discussed in previous statement,above we store the (length of 'prod' variable) in (n). 
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        #as discussed inside (index) function only that above finction will gives us the (no. of slides) of (4 cards or products each).
        if len(prod)!= 0:
            #see the above (if) statement checks if the (prod) variable  is empty or not.as discussed in previous statements that it'll be empty when there is no match between the product (searched by user) and (the products we have in our shop.).IF THE (prod) VARIABLE IS NOT EMPTY THE BELOW STATEMENTS WILL GET EXECUTED.
            allProds.append([prod, range(1, nSlides), nSlides])
    #NOW ALL THIS BELOW LOGIC IS SIMILAR TO WHAT WE HAVE DONE IN (INDEX) FUNCTION.IT WILL JUST DISPLAY ALL THE PRODUCTS IN (PROD) VARIABLE.
    params = {'allProds': allProds, "msg":""}
    if len(allProds)==0 or len(query)<4:
        params={'msg':"Please make sure to enter relevant search query"}
        #above message is displayed when the user enters irrelevent query in search box.
    return render(request, 'shop/search.html', params)
#In the above code, we're storing the user's query in the query variable, and then we will check if the user query matches any product on our E-commerce website. We're using a searchMatch function to check if the user query matches with items or not. This function will return a boolean value. Type the below code to create the searchMatch function :

def about(request):
    return render(request,"shop/about.html")

def contact(request):
    thank=False
    #In the above code, we've initially set the thanks variable to false, so whenever the user submits the response, the function will execute, and the false value will be turned to true. 
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank=True
    return render(request, 'shop/contact.html', {'thank':thank})

#below (tracker) function is rensponsible for displaying all the  dettails related to a particular (order_id) in the (tracker.html) page.
def tracker(request):
    if request.method=="POST":
        #this if block will get executed when the data (i.e, 'order_id' and 'email') related to a particular order are successfully stored into the database (using 'POST' method).it simply means the data entered by user on "tracker.html" page is successfully saved in database. 
        orderId = request.POST.get('orderId', '')
        #then the above statement will store the (order_id).
        email = request.POST.get('email', '')
        #and above will store its email.

        #below try and catch statement blocks will check if the details of a particular (order_id) that the user is seeking ,exists or not.just for error handling.
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            #above we take the (id and email) of that particular (order_id) whose details is seeked by user,and store it in an (order) variable.
            if len(order)>0:
                #if the len(length or count) of that product(at particular order_id) is greater than 0,then obviously that order exists and it is valid.so below we can proceed further:
                update = OrderUpdate.objects.filter(order_id=orderId)
                #in above (update) variable we take the (id) of that particular (order) whose details is seeked by user on 'tracker.html' page.
                updates = []
                #above we create an empty list[] named "updates". 
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    #above we add  the data in(updates) (which we are trying to make a json file) and the data is decription of a product(update_desc) and time.

                    response = json.dumps([updates, order[0].items_json],default=str)
                    #If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.so the above statement is converting the data in json file(i.e, decription of a product(update_desc) and time).
                    #we modified the above code a bit and as discussed in above comment we are are converting the data in (updates) as well as the the value of (items_json) at [0th] index.
                return HttpResponse(response)
                #and above statement will send the (response) to the 'tracker.html' page where it will be displayed in some way. also as stated in the previous statement,(response) is now converted to "string" and to send a string we use (HttpResponse) in (return) statement. 
            else:
                return HttpResponse('{}')
                #same as below except statement.
        except Exception as e:
            #so if the (try) block is not executed the below return statement will return an empty statement({}) as a 'string'(as we know HttpResponse is used to return a string).
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')



def productView(request, myid):
    #Fetching the product using its id.
    product=Product.objects.filter(id=myid)
    # above we store the product at particular id (i.e, the the value of "myid" as returned by (path variable) of "urls.py") page and which is nothing but the "id of product whose QUICKVIEW button is pressed by user").also above "product" variable is a list so below,in the "return" statement we have given product at [0]th index,its ovious there will be only 1 element in the list as the list has to contain product of a paricular id,but still it is a list so all these. 
    print(product)
    # above we print the same product,which can be seen in browser's console.
    return render(request,"shop/productView.html", {'product':product[0]})


#below stuff for checkout function.
def checkout(request):
    if request.method=="POST":
        items_json= request.POST.get('itemsJson', '')
        #upar waale column me har order ki (json) file store hogi.json me kuch nahi bas order details hi hai dictionary{ke:value}pair ke roop me.
        name=request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        #above will get the (amount) from (amount) placeholder on (checkout.html) page and save it as a single {dictionary} value having 'amount' as its 'key'.this,with others,will be saved in the (order) variable velow and (saved) into the database(using 'order.save()'). ONCE WE HAVE ENTERED ALL THE DETAILS ON (checkout.html) page and get the thanks message,then we can see the (admin) page and we'll find that,thier the (amount) column will have the same value as we have seen on the "checkout.html" page while saving the particular order. 
        email=request.POST.get('email', '')
        address=request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')

        order = Orders(items_json= items_json, name=name, email=email, address= address, city=city, state=state, zip_code=zip_code, phone=phone,amount=amount)
        order.save()
        #above statement will save all details relating to a particular order (as stored in (order) variable above)  into the DATABASE.

        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        #above (update) variable has two parameters one is the (order_id) and then is some string ("The order has been placed") which will be sent to (order_id) and (update_desc) columns of (OrderUpdate) table or model.
        update.save()
        #above will save the above  things to the DATABASE.

        thank=True
        #after (order) variable is stored in database,above statement will make the value of (thank) variable as"true".
        id=order.order_id
        #return render(request, 'shop/checkout.html', {'thank':thank, 'id':id})
        #see when the order details of user from "checkout" page is successfully saved in our database,the above statement will generate (thank)  and the (id) of that user as an (arguement) and send it to the "checkout.html" page  where a function will help to display a "thank you" message to the user having particular "id".
        #****************************************

        # Request paytm to transfer the amount to your account after payment by user.ye paytm ko request bhejega ki ye sab details le lo aur verify karke,payment hone ke baad mujhe mere account me paise bhej dena.
        param_dict = {
            #this {dictinary} stores all the details that will be sent to paytm.this is also from paytm only.

                # ???????? the problem is here in this below key's length.i think we need to first create our own paytm merchant account and try with our merchant key.
                'MID': 'Your-Merchant-Id-Here',#WorldP64425807474247
                #above is merchant id and dbelow is order id.but in production site you'll use the valid merchant id and key given to you by paytm.look for this error in the terminal too: File "C:\python 311\Lib\site-packages\Crypto\Cipher\AES.py", line 90, in _create_base_cipher raise ValueError("Incorrect AES key length (%d bytes)" % len(key)) ValueError: Incorrect AES key length (22 bytes)    ....AND LOOK AT THE LINES IN ERROR MENTIONED THIER.

                #below both values being entered in these columns are converted to strings using 'str' function. 
                'ORDER_ID': str(order.order_id),
                'TXN_AMOUNT': str(amount),
                #as stated below ,customer's id will be his/her email.
                'CUST_ID': email,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                #above we give value as "WEBSTAGING" for testing purpose. i.e, we won't make actual payments
                'CHANNEL_ID': 'WEB',
                #now paytm will tell us whether the  payment is done or not in below url or address or page of our site.
                'CALLBACK_URL':'http://127.0.0.1:8000/shop/handlerequest/',

        }
        # in the below dictionary (param_dict) we create a new {key} called 'CHECKSUMHASH' and we'll it a checksum value using [Checksum.generate_checksum(param_dict, MERCHANT_KEY)] ,(it simply generates a checksum by taking arguemnts (an dictionary)like(param_dict) and the(MERCHANT_KEY)).
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        #below we are sending the (param_dict) dictionary to "shop/paytm.html" page.
        return render(request, 'shop/paytm.html', {'param_dict': param_dict})

    return render(request, 'shop/checkout.html')

#NOW THE (crsfexempt) module imported and explained above will exempt the (functionality) of (crsf) token in the below portion only.
@csrf_exempt
#below we'll handle the (request)(i.e,Post request) sent by payTM after the payment is done.
def handlerequest(request):
    # paytm will send you post request here and BELOW WE STORE IT IN FORM (WHICH IS A DICTIONAY).
    form = request.POST
    #AN EMPTY DICTIONARY BELOW.
    response_dict = {}
    for i in form.keys():
        #BELOW WE TAKE AND ADD ALL THE PARAMETERS OF RESPONSE BY PAYTM TO RESPONSE_DICT.
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
    #BELOW WE VERIFY THE CHECKSUM BY CHECKING IF BOTH THE CHEKSUM SENT BY US TO PAYTM AND SENT BY PAYTM IS SAME OR NOT.IF NO ONE HAS HAMPERED IT THEN THE COMPARISON SHOULD GIVE '01' OR 'TRUE'. 
    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    #THE PAYMENT RESULT STATUS CHECKED ABOVE WILL BE SENT TO "shop/paymentstatus.html" PAGE.
    return render(request, 'shop/paymentstatus.html', {'response': response_dict})


##### >>>>>>>>>>>SEE EVEN THOUGH ALL THESE CODE IS FOR FREE FROM PAYTM, IT IS NOT EASY TO WORK WITH THEM AT FIRST.SOMETIMES THE CODE HAS MANY ERRORS AND WON'T WORK ,SO LIKE HARRY WE NEED TO READ THEN INFO PROVIDED BY THEM ON THIER SITE FROM WHERE WE HAVE COPIED THIS CODE AND MAKE CHANGES ACCORDINGLY.HE HAS SIMPLIED THOSE CODE AND MADE THEM ACCORDING TO DJANGO

####>>>>>>>>>>> see here we had some errors while running the server in command prompt as it was showing that there is no (paytm) module.now this was because we have saved the folder with name (PayTm) and not paytm. similarly the file inside this folder was named (checksum) instead of (Checksum),so try to check these simple things also if any error occurs.