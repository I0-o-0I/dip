# Generated by Django 5.1.4 on 2024-12-23 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_menuhotter_menusalads_delete_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='menusalads',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]