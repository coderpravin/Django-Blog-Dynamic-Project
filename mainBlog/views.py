from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Category, Blog
from assignment1.models import About, SocialLink
from django.db.models import Q
import logging
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout 
#create logging here
logging.basicConfig(filename='sample.log',
                    
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
    categories  = Category.objects.all()
    featured_post = Blog.objects.filter(is_featured=True)
    abouts = About.objects.get(id=1)
    sociallink = SocialLink.objects.all()

    #posts = Blog.objects.filter(status="Published")
    posts = Blog.objects.filter(is_featured=False, status="Published")
    print("Posts",posts)
    logger.debug(f"Home page called")
    context = {
        
         'categories':categories,
         'featured_post':featured_post,
         'posts' : posts,
         'abouts' : abouts,
         'sociallink' : sociallink,
        }
    return render(request, 'mainBlog/home.html', context)


def category_id(request,pk):
    print("The pk is", pk)
    post = Blog.objects.filter(is_featured= True, pk=pk)
    category = get_object_or_404(Category, pk=pk)
    #category = Category.objects.get(pk=pk)
    context = {
        'post' : post,
        'category' : category
    }
    return render(request, 'mainBlog/category_by_id.html', context)
    


def blog_info_id(request,pk):
    blog = get_object_or_404(Blog, pk=pk)
    context = {
        'blog' : blog
    }
    return render(request, 'mainBlog/blog_by_id.html', context)


def single_Blog_Slug(request,slug):
    blog = get_object_or_404(Blog, slug=slug)
    social_links = SocialLink.objects.all()
    context = {
        'blog':blog,
        'social_links' : social_links,
    }
    return render(request,'mainBlog/blog_by_slug.html', context)

def search_blog(request):
    keyword = request.GET.get('keyword','')
    
    blogs = Blog.objects.filter(Q(title__icontains = keyword)|
                        Q(short_information__icontains = keyword)|
                        Q(blog_body__icontains = keyword))
    
    context = {
        'blogs' : blogs,
        'keyword' : keyword
    }
    
    return render(request, 'mainBlog/search_blog.html', context)
    
    
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginUser')
        else:
            print(form.errors)
    else:
        
        form = RegistrationForm()
    context = {
        'form' : form
    }
    return render(request, 'mainBlog/register.html', context)

def loginUser(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password =  form.cleaned_data.get('password')
            
            user = authenticate(username = username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect("home")
        
            
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'mainBlog/login.html', context)

def logoutuser(request):
    logout(request)
    return redirect('home')