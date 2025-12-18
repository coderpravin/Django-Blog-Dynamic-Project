from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('category/<int:pk>', views.category_id),
    path('blog/<int:pk>', views.blog_info_id, name="blog_info"),
    path('slugblog/<slug:slug>', views.single_Blog_Slug, name="blog-by_slug"),
    path('search_blog', views.search_blog, name="search_blog"),
    
    #Register Url Here
    path('register', views.register, name="register"),
    path('loginUser', views.loginUser, name="loginUser"),
    path('logoutuser', views.logoutuser, name="logoutuser"),
]
