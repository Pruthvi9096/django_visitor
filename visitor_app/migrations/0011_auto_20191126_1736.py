# Generated by Django 2.2.7 on 2019-11-26 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor_app', '0010_visitor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
