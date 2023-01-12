from django.contrib import admin

from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'body']
    list_display = ['title', 'slug', 'category', 'pub_date']
    list_filter = ['category', 'pub_date']

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category)