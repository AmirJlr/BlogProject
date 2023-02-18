from django.contrib import admin
from .models import Category, Post


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'active']
    list_filter = ('active',)

    search_fields = ('title',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'status', 'publish_time')
    list_filter = ('category', 'author', 'status', 'publish_time')
    search_fields = ('title', 'lead', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish_time'
    raw_id_fields = ('author',)

