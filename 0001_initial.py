# Generated by Django 4.2.5 on 2023-09-18 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import library.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('isbn', models.PositiveIntegerField()),
                ('author', models.CharField(max_length=40)),
                ('category', models.CharField(choices=[('education', 'Education'), ('entertainment', 'Entertainment'), ('comics', 'Comics'), ('biography', 'Biographie'), ('history', 'History')], default='education', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='IssuedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment', models.CharField(max_length=30)),
                ('isbn', models.CharField(max_length=30)),
                ('issuedate', models.DateField(auto_now=True)),
                ('expirydate', models.DateField(default=library.models.get_expiry)),
            ],
        ),
        migrations.CreateModel(
            name='StudentExtra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment', models.CharField(max_length=40)),
                ('branch', models.CharField(max_length=40)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
