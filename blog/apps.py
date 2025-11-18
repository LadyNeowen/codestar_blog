"""
Configuration for the Blog application.

This module defines the BlogConfig class, which provides metadata
and configuration options for the blog app within the Django project.
"""

from django.apps import AppConfig


class BlogConfig(AppConfig):

    """
    AppConfig for the blog app.

    Attributes:
        default_auto_field: Specifies the type of primary key field to use
            for models that do not explicitly define one.
        name: The full Python path to the application.
    """
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
