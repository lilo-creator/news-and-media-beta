# Generated by Django 5.2.1 on 2025-07-28 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='featured_image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
