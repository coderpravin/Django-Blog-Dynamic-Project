from django.contrib import admin
from .models import Category, Blog
# Register your models here.
admin.site.register(Category)


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title', )}
    list_display = ('title','category', 'author','status', 'is_featured')
    search_fields = ('id', 'title', 'category__category_name', 'author__username')
admin.site.register(Blog, BlogAdmin)