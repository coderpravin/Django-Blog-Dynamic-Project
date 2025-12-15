from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Blog
from assignment1.models import About, SocialLink
import logging

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
    context = {
        'blog':blog,
    }
    return render(request,'mainBlog/blog_by_slug.html', context)
