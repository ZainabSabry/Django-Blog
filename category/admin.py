from django.contrib import admin
from .models import Category, Post, BlockedWords, Comment


class InlinePost(admin.StackedInline):
    model = Post
    extra = 1


class CustomCategory(admin.ModelAdmin):
    inlines = [InlinePost]


class CustomPost(admin.ModelAdmin):
    fieldsets = (
        ['write a new post', {'fields': ['title', 'slug', 'author','tags']}],
        ['post content', {'fields': ['content', 'image']}],
        ['Publish date', {'fields': ['publish_date']}]
    )
    list_display = ('title', 'slug', 'author', 'content', 'publish_date')
    search_fields = ('title', 'slug', 'author')
    list_filter = ('title',)


class CustomBlockedWords(admin.ModelAdmin):
    fieldsets = (
        ['new blocked words', {'fields': ['words']}],

    )
    search_fields = ('words', )


admin.site.register(Category, CustomCategory)
admin.site.register(Post, CustomPost)
admin.site.register(BlockedWords, CustomBlockedWords)
admin.site.register(Comment)