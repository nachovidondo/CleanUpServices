# Generated by Django 3.1.3 on 2022-03-22 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_app', '0004_portfolio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(upload_to='Portfolio_images'),
        ),
    ]
