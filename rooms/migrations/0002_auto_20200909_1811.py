# Generated by Django 3.1.1 on 2020-09-09 09:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='address',
            field=models.CharField(max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='baths',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='bedrooms',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='beds',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='check_in',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='check_out',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='city',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='guests',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='host',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='instant_book',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
