from django.db import models
from django.utils import timezone
from markdownx.models import MarkdownxField

class HomeArticle(models.Model):
    title = models.CharField(max_length=40)
    summary = models.TextField(blank=False)
    text = MarkdownxField('本文', help_text='Markdown形式で書いてください。')
    date = models.DateTimeField(blank=False)

    def __str__(self):
        return self.title



