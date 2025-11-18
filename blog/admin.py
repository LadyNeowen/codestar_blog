"""
Admin configuration for the Post and Comment models.

This module customizes how the Post and Comment models appear and
behave inside the Django admin interface. It includes Summernote
integration for rich-text editing on Post content.
"""

from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    """
    Admin interface configuration for the Post model.

    Features:
        - Displays key Post fields in the admin list view (title, slug,
          status, created_on).
        - Allows searching posts by title and content.
        - Enables filtering by status and creation date.
        - Automatically generates the slug field from the title.
        - Uses Summernote rich-text editor for the 'content' field.
    """

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.

admin.site.register(Comment)
