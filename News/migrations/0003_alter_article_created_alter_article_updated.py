# Generated by Django 5.2.1 on 2025-07-22 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_article_created_article_updated_article_view_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
