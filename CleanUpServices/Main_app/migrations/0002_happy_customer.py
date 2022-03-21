# Generated by Django 3.1.3 on 2022-03-21 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Happy_Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images_uploaded')),
                ('description', models.TextField()),
            ],
        ),
    ]
