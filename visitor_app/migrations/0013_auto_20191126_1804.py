# Generated by Django 2.2.7 on 2019-11-26 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor_app', '0012_auto_20191126_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='image',
            field=models.FilePathField(path='/gallery'),
        ),
    ]
