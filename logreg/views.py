from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
#Importing django inbuilt authentication system
from django.contrib.auth.models import User, auth
from django.contrib import messages
from blog.forms import PostForm
from blog.models import Post

# Create your views here.

#Create a login view
def login(request):
    #Using an IF statement to render if there's a POST request method
    if request.method== 'POST':
        #Getting the Username and Password from the request
        username = request.POST['username']
        password = request.POST['password']

        #Using the authenticate function to check if the username and password matches with that in the database
        user = auth.authenticate(username=username, password=password)
        
        #If user details is correct
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        #If user details aren't correct
        else:
            #Parsing a message in the template
            messages.info(request, 'Invalid Credentials')
            return render(request, 'logreg/login.html')
    #If the request method is GET
    else:
        return render(request, 'logreg/login.html')

#Making a signup view
def signup(request):
    #If the method is POST
        if request.method == 'POST':
            #Gathering the registration inputs from the form
            first_name = request.POST['firstname']
            last_name = request.POST['lastname']
            username = request.POST['username']
            email = request.POST['email']
            Password = request.POST['password']
            Password2 = request.POST['password2']

            #If statement to make sure that the password is confirmed
            if Password==Password2:
                #Using an if statement to check if an email already exists
                if User.objects.filter(email=email).exists():
                    #Output message
                    messages.info(request, 'Email already exists')
                    return redirect('signup')
                #Using an if statement to check if a username already exists
                elif User.objects.filter(username=username).exists():
                    #Output message
                    messages.info(request, 'Username already exists')
                    return redirect('signup')
                #If the above if statements are false
                else:
                    #Creating a user with the information given
                    user= User.objects.create_user(username=username,email=email,password=Password, first_name=first_name, last_name= last_name )
                    #Saving user
                    user.save();
                    #Output message
                    messages.info(request, 'Account successfully created!')
                    return redirect('login')
            else:
                messages.info(request, 'Password does not match!')
                return redirect('signup')
        else:
            return render(request, 'logreg/signup.html')

#Creating a logout view
def logout(request):
    #Using the logout function
    auth.logout(request)
    return redirect('/')


#Create a post creation view
def create(request):
    #Using the Postform ModelForm and parsing it into the template as context
    form = PostForm()
    context = {'form' : form}
    #Output if user is authenticated
    if request.user.is_authenticated:
        #Request method is GET
        if request.method == 'POST':
            #Using the Post Model
            a = Post()
            #Collecting the data and files passed into the form
            form = PostForm(request.POST, request.FILES)
            #Saving the information in writer but not sending data into the database (Commit = False)
            writer = form.save(commit= False)
            #Adding author field from the request.user since it could not be passed from the form
            writer.author = request.user
            #Save
            writer.save()

            #Output message
            messages.info(request, 'You have successfully created a blog')
            return redirect("/")

        return render(request, 'logreg/create.html', context)
        
    #If the user clicked the create post link but was not logged in
    else:
        messages.info(request, 'You have to be logged in first!')
        return redirect('login')

#Creating a like view and importing the request and id 
def like(request,id):
    #Get the Post which matches the id requested
    Posts= Post.objects.get(id=id)
    #Output if user is authenticated
    if request.user.is_authenticated:
        #If the current user has already exists as someone who had liked the post
        if Posts.liked.filter(id=request.user.id).exists():
            is_liked = False
            #Remove from the list of likers
            Posts.liked.remove(request.user)
        
        #If current user has not liked the post
        else:
            is_liked = True
            #Add the like based on the user
            Posts.liked.add(request.user)
            Posts.save()
        return redirect('/')
    else:
        messages.info(request, 'You have to be logged in first!')
        return redirect('login')
