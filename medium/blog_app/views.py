from django.shortcuts import render
from blog_app.forms import CategoryForm,UserForm,UserProfileForm,PostForm,UserUpdateInfoForm
from blog_app.models import Category,Post,last_4_posts,Profile
from django.contrib.auth.models import User

from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
# Create your views here.

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

def index(request):
    category = Category.objects.all()[:5]
    editor_posts = Post.objects.filter(editor_choice=True).order_by('-date_created')[:1]
    trending_posts = Post.objects.order_by('-upvote')[:1]
    new_posts_for_all = Post.objects.order_by('-date_created')[:3]
    popular_on_medium = Post.objects.order_by('-upvote')[:3]
    # new_from_network = Post.objects.filter(category = request.user.profile.topic1) | Post.objects.filter(category = request.user.profile.topic2) | Post.objects.filter(category = request.user.profile.topic3)
    if request.user.is_authenticated:
        new_from_network = Post.objects.filter(Q(category=request.user.profile.topic1) | Q(category=request.user.profile.topic2) | Q(category=request.user.profile.topic3)).order_by('-date_created')[:3]
    else:
        new_from_network = "Login to view this section"

    if request.user.is_authenticated:
        last1 = request.user.last_4_posts.post1
        last2 = request.user.last_4_posts.post2
        last3 = request.user.last_4_posts.post3
        last4 = request.user.last_4_posts.post4

        author1 = Post.objects.filter(id=last1)
        author2 = Post.objects.filter(id=last2)
        author3 = Post.objects.filter(id=last3)
        author4 = Post.objects.filter(id=last4)

        for post in author1:
            author1_name = post.author
        for post in author2:
            author2_name = post.author
        for post in author3:
            author3_name = post.author
        for post in author4:
            author4_name = post.author

        based_on_your_view = Post.objects.filter(Q(category=request.user.profile.topic1) | Q(category=request.user.profile.topic2) | Q(category=request.user.profile.topic3) | Q(author=author1_name) | Q(author=author2_name) | Q(author=author3_name) | Q(author=author4_name)).order_by('-date_created')[:10]
    else:
        based_on_your_view = Post.objects.all().order_by('-date_created')[:10]
    
    if request.user.is_authenticated:
        reading_list = Post.objects.filter(category=request.user.profile.topic1).order_by('-date_created')[:2]
    else:
        reading_list = "Login to view your reading list"

    cat_dict = {'category':category,'count':0,'editor_choice':editor_posts,'trending_posts':trending_posts,'new_posts_for_all':new_posts_for_all,'new_from_network':new_from_network,'popular_on_medium':popular_on_medium,'based_on_your_view':based_on_your_view,'reading_list':reading_list}
    return render(request,"blog_app/index.html",context=cat_dict)

def create_category(request):
    form = CategoryForm()
    msg = ''
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            msg='created'
            #return index(request)
        else:
            print("Error in form")
    return render(request,'blog_app/create_category.html',{'form':form,'msg':msg})

def register(request):
    registerd = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data = request.POST)
        

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            last4Posts = last_4_posts.objects.create()
            last4Posts.user = user
            last4Posts.save()

            registerd = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,'blog_app/registration.html',{'user_form':user_form,'profile_form':profile_form,'registerd':registerd})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse(index))
            else:
                return HttpResponse("Your Account is Not Active")
        else:
            return HttpResponse("Invalid Login Details Supplied")
    else:
        return render(request,'blog_app/login.html',{})

def add_post(request):
    form = PostForm()
    msg = ""
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            if 'poster' in request.FILES:
                obj.poster = request.FILES['poster']
            obj.author = request.user.username
            obj.organisation = request.user.profile.organisation
            obj.author_image = request.user.profile.profile_pic
            obj.save()
            msg='created'
        else:
            msg = "Not Submitted"
    else:
        form = PostForm()
        msg=''
    return render(request,'blog_app/add_post.html',{'form':form,'msg':msg})

def cat_details(request,value):
    category = Category.objects.all()[:5]
    topic = Category.objects.filter(topic=value)
    t_id = 0
    for t in topic:
        t_id = t.id
    
    category_posts = Post.objects.filter(category=t_id).order_by('-date_created')
    category_editor_post = Post.objects.filter(category=t_id).filter(editor_choice=True).order_by('-date_created')[:4]
    return render(request,'blog_app/cat_details.html',{'topic':value,'category':category,'category_posts':category_posts,'category_editor_post':category_editor_post})


def post_details(request,value):
    category = Category.objects.all()[:5]
    posts = Post.objects.filter(id=value).order_by('-date_created')

    #update the post being watched
    if request.user.is_authenticated:
        last_posts = last_4_posts.objects.get(user = request.user)
        if request.user.profile.replacer == 1:
            if last_posts.post1 != value:
                last_posts.post1 = value
        elif request.user.profile.replacer == 2:
            if last_posts.post2 != value:
                last_posts.post2 = value
        elif request.user.profile.replacer == 3:
            if last_posts.post3 != value:
                last_posts.post3 = value
        else:
            if last_posts.post4 != value:
                last_posts.post4 = value
        request.user.profile.replacer = (request.user.profile.replacer + 1)%4
        if request.user.profile.replacer == 0:
            request.user.profile.replacer = 4
        last_posts.save()
        request.user.profile.save()    
        
    return render(request,'blog_app/post_detail.html',{'post_id':value,'posts':posts,'category':category})

@login_required
def update_profile(request):
    user1 = request.user
    profile = request.user.profile
    if request.method == "POST":
        user_form = UserUpdateInfoForm(request.POST,instance=User.objects.get(pk=int(request.user.id)))
        p_id = request.user.profile.id
        profile_form = UserProfileForm(request.POST,instance=Profile.objects.get(pk=int(p_id)))

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=True)

            # Hash the password
            #user.set_password(user.password)

                # Update with Hashed password
            #user.save()

                # Now we deal with the extra info!

                # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

                # Set One to One relationship between
                # UserForm and UserProfileInfoForm
            profile.user = user

                # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                    # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

                # Now save model
            profile.save()
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserUpdateInfoForm(instance=User.objects.get(pk=int(request.user.id)))
        p_id = request.user.profile.id
        profile_form = UserProfileForm(instance=Profile.objects.get(pk=int(p_id)))
    return render(request,'blog_app/update_profile.html',{'user_form':user_form,'profile_form':profile_form})

def more_posts(request):
    categories = Category.objects.all()
    return render(request,'blog_app/more_post.html',{'categories':categories})