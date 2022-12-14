# Generated by Django 3.2.7 on 2022-09-18 21:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('image', models.ImageField(upload_to='ads/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('ad_type', models.CharField(choices=[('banner', 'Banner'), ('block', 'Block'), ('popup', 'Popup')], max_length=50)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
