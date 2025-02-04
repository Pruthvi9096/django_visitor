# Generated by Django 2.2.7 on 2019-11-19 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('address', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='VisitFor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitor_app.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_phone', models.CharField(max_length=20)),
                ('visitor_email', models.EmailField(max_length=250)),
                ('purpose', models.CharField(max_length=150)),
                ('checkOut_time', models.DateTimeField(auto_now=True)),
                ('checkIn_time', models.DateTimeField(auto_now_add=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitor_app.Department')),
                ('visit_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitor_app.VisitFor')),
                ('visitor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitor_app.Visitor')),
            ],
        ),
    ]
