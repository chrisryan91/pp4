# Generated by Django 3.2.23 on 2024-01-02 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pp4app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='featured_image_b',
            field=models.URLField(blank=True, max_length=5000, null=True),
        ),
    ]
