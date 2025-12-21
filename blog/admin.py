from django.contrib import admin
from .models import Post, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'published_at')
    list_filter = ('status', 'category')
    search_fields = ('title', 'excerpt', 'content')
    readonly_fields = ('published_at',)

    fields = (
        'title',
        'slug',
        'category',
        'status',
        'excerpt',
        'content',
        'image',
        'published_at',
    )

    prepopulated_fields = {'slug': ('title',)}
