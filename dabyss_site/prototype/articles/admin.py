from django.contrib import admin
from .models import HomeArticle
from markdownx.admin import MarkdownxModelAdmin

admin.site.register(HomeArticle, MarkdownxModelAdmin)
