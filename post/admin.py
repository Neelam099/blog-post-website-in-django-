
from django.contrib import admin
from .models import BlogPost, Comment
# Register your models here.


class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment)