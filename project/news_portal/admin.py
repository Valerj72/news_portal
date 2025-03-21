from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *



class CategoryInline(admin.TabularInline):
    model = PostCategory
    extra = 1


class PostAdmin(admin.ModelAdmin):
    model = Post
    inlines = (CategoryInline,)
    list_display = ('id', 'article_title', 'preview', 'time_in', 'categories', 'rating', 'like', 'dislike',)
    list_display_links = ('article_title',)
    list_filter = ('author', 'category', 'time_in',)
    search_fields = ('article_title', 'article_text', 'author__user__username', 'rating')

    def preview(self, obj):
        return obj.preview

    def categories(self, obj):
        return ", ".join([cat.name for cat in obj.category.all()])

    preview.short_description = 'Содержание'
    categories.short_description = 'Категории'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment_text', 'user', 'time_in', 'rating', 'post')
    list_display_links = ('comment_text',)
    list_filter = ('user', 'post',)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'rating')
    list_display_links = ('user',)


class TransCategoryAdmin(TranslationAdmin):
    model = Category


class TransPostAdmin(PostAdmin, TranslationAdmin):
    model = Post


admin.site.register(Post, TransPostAdmin)
admin.site.register(Category, TransCategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Author, AuthorAdmin)

