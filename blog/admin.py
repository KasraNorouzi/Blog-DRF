from django.contrib import admin
from blog.models import Post, Category


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'slug', 'category',
                    'status', 'published_date', 'created_date')


admin.site.register(Post)
admin.site.register(Category)