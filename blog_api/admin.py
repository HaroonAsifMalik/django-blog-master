from django.contrib import admin
from blog.models import Post, Category


@admin.register(Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'slug', 'author')
    prepopulated_fields = {'slug': ('title',), }  # it can automaticaly populated based on title field


admin.site.register(Category)