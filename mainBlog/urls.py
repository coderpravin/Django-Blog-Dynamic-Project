from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('category/<int:pk>', views.category_id),
    path('blog/<int:pk>', views.blog_info_id),
    path('slugblog/<slug:slug>', views.single_Blog_Slug, name="blog-by_slug"),
]
