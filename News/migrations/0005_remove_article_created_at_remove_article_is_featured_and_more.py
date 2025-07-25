# Generated by Django 5.2.1 on 2025-07-23 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0004_alter_article_content_alter_article_excerpt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='article',
            name='is_featured',
        ),
        migrations.RemoveField(
            model_name='article',
            name='likes_count',
        ),
        migrations.RemoveField(
            model_name='article',
            name='reading_time',
        ),
        migrations.RemoveField(
            model_name='article',
            name='share_count',
        ),
        migrations.RemoveField(
            model_name='article',
            name='thumbnail',
        ),
        migrations.RemoveField(
            model_name='article',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='article',
            name='views_count',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='ip_address',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='reported',
        ),
        migrations.AlterField(
            model_name='article',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
