# Generated by Django 5.0.1 on 2024-02-14 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_delete_hospitalname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='hospital_image',
            field=models.ImageField(upload_to='hospital_images'),
        ),
    ]
