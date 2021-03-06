# Generated by Django 3.0.7 on 2020-06-18 07:38

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('summary', models.TextField(verbose_name='概要')),
                ('text', markdownx.models.MarkdownxField(help_text='Markdown形式で書いてください。', verbose_name='本文')),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='GamesArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('summary', models.TextField(verbose_name='概要')),
                ('text', markdownx.models.MarkdownxField(help_text='Markdown形式で書いてください。', verbose_name='本文')),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='homearticle',
            name='summary',
            field=models.TextField(verbose_name='概要'),
        ),
    ]
