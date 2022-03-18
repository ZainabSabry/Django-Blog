from django.contrib import admin
from .models import Category, Post


class InlinePost(admin.StackedInline):
    model = Post
    extra = 1


class CustomCategory(admin.ModelAdmin):
    inlines = [InlinePost]


class CustomPost(admin.ModelAdmin):
    fieldsets = (
        ['write a new post', {'fields': ['title', 'slug', 'author']}],
        ['post content', {'fields': ['content']}],
        ['Publish date', {'fields': ['publish_date']}]
    )
    list_display = ('title', 'slug', 'author', 'content', 'publish_date')
    search_fields = ('title', 'slug', 'author')
    list_filter = ('title', )


admin.site.register(Category, CustomCategory)
admin.site.register(Post, CustomPost)
