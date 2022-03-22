# Generated by Django 3.1.3 on 2022-03-21 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images_uploaded')),
                ('description', models.TextField()),
                ('video', models.FileField(blank=True, null=True, upload_to='videos_uploaded')),
            ],
        ),
    ]