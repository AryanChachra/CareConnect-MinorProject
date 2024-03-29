# Generated by Django 5.0.1 on 2024-02-09 09:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(max_length=200)),
                ('Fathers_Name', models.CharField(max_length=200)),
                ('Gender', models.CharField(max_length=200)),
                ('Email', models.CharField(max_length=200, unique=True)),
                ('Password', models.TextField()),
                ('Address1', models.TextField()),
                ('Address2', models.TextField()),
                ('City', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('zip', models.IntegerField()),
                ('User', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
