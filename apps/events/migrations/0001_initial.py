# Generated by Django 3.2.7 on 2023-09-12 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=124)),
                ('description', models.TextField()),
                ('start_at', models.DateTimeField(auto_now_add=True)),
                ('end_at', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(max_length=124)),
                ('image', models.ImageField(upload_to='post/images')),
                ('price', models.PositiveIntegerField(default=0)),
                ('registration', models.URLField(max_length=123)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
