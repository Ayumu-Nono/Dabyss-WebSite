# Generated by Django 3.0.7 on 2020-06-18 07:05

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('summary', models.TextField()),
                ('text', markdownx.models.MarkdownxField(help_text='Markdown形式で書いてください。', verbose_name='本文')),
                ('date', models.DateTimeField()),
            ],
        ),
    ]