# Generated by Django 3.2.7 on 2022-09-18 21:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='art/')),
                ('title', models.CharField(max_length=255)),
                ('order', models.IntegerField(default=1)),
                ('custom_display_name', models.CharField(blank=True, max_length=200, null=True)),
                ('original_work', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('artist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', tinymce.models.HTMLField(blank=True, null=True)),
                ('special_link', models.URLField(blank=True, null=True)),
                ('featured', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('custom_issue_editor', models.CharField(blank=True, max_length=200, null=True)),
                ('custom_art_editor', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateField(blank=True, help_text='Written as YYYY-MM-DD', null=True)),
                ('art_editor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='art_editor', to=settings.AUTH_USER_MODEL)),
                ('cover_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='read.artwork')),
                ('issue_editor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='issue_editor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', tinymce.models.HTMLField(blank=True, null=True)),
                ('created_at', models.DateField(blank=True, help_text='Written as YYYY-MM-DD', null=True)),
                ('voice_file', models.FileField(blank=True, null=True, upload_to='voices/')),
                ('active', models.BooleanField(default=True)),
                ('classic', models.BooleanField(default=False)),
                ('custom_display_name', models.CharField(blank=True, help_text='Leave blank if you want your name to show up', max_length=200, null=True)),
                ('featured', models.BooleanField(default=False)),
                ('laugh_score', models.PositiveBigIntegerField(default=0)),
                ('original_work', models.BooleanField(default=True)),
                ('art_work', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='works', to='read.artwork')),
                ('magazine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='works', to='read.magazine')),
                ('writer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cookie', models.CharField(max_length=255, null=True)),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='views', to='read.work')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('year_published', models.CharField(max_length=4)),
                ('seller_link', models.URLField()),
                ('active', models.BooleanField(default=True)),
                ('description', tinymce.models.HTMLField()),
                ('created_at', models.DateField(blank=True, help_text='Written as YYYY-MM-DD', null=True)),
                ('cover_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='read.artwork')),
            ],
        ),
    ]
