from django.shortcuts import render
from django.http import HttpResponse

from .models import Blogpost

# Create your views here.

 #we will develop logic to display the blog on the home page of the blog app. So without wasting time, open the views.py file of the blog app and type the below code :
def index(request):
    myposts= Blogpost.objects.all()
    #in above (mypost) variable we store all (blogs) present in (Blogpost).
    print(myposts)
    #above we print the same.can be seen in console.
    return render(request, 'blog/index.html', {'myposts': myposts})
    #In the above code, we are storing all the objects of the Blogpost in a variable named myposts. After then, we are printing all the objects on the terminal(this step is optional). In the end, we are rendering mypost as a dictionary to the index.html template. Now, we will use the for loop in the index.html file to display the blog posts on the home page.
    # above "index.html" is inside the (blog) folder so we wrote "blog/index.html".

def blogpost(request, id):
    #above we'll get the (id) of the (blog) seeked by the user and below we store the (post) at that particular id in (post) variable.
    post = Blogpost.objects.filter(post_id = id)[0]
    print(post)

    #below in the return statement we return the same particular (post) as discussed above.
    return render(request, 'blog/blogpost.html',{'post':post})
#In the above code, we've passed the (blog id) that we fetched from the "URLs.py" page. After this, we filter the blog post using objects.filter, and in the end, we've passed the post variable in the render function.