# Generated by Django 5.0.1 on 2024-03-31 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_alter_profiledata_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beds',
            name='Disease',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='beds',
            name='Room_number',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='beds',
            name='Ward_number',
            field=models.CharField(max_length=100),
        ),
    ]