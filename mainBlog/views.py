from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Blog
import logging

#create logging here
logging.basicConfig(filename='sample.log',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
    categories  = Category.objects.all()
    featured_post = Blog.objects.filter(is_featured=True)
    logger.debug(f"Home page called")
    context = {
         'categories':categories,
         'featured_post':featured_post
        }
    return render(request, 'mainBlog/home.html', context)


