# Generated by Django 5.0 on 2023-12-19 17:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cabin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creted_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=255)),
                ('max_capacity', models.SmallIntegerField()),
                ('regular_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('discount', models.DecimalField(decimal_places=3, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creted_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('nationality', models.CharField(max_length=255)),
                ('country_flag', models.CharField(max_length=255)),
                ('national_id_number', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creted_at', models.DateTimeField(auto_now=True)),
                ('min_booking_length', models.IntegerField()),
                ('max_booking_length', models.IntegerField()),
                ('max_guest_per_booking', models.IntegerField()),
                ('breakfast_price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creted_at', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('nights_number', models.SmallIntegerField()),
                ('guests_number', models.SmallIntegerField()),
                ('cabin_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('extra_price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('status', models.CharField(max_length=255)),
                ('has_breakfast', models.BooleanField()),
                ('is_paid', models.BooleanField()),
                ('observations', models.TextField(null=True)),
                ('cabin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel_api.cabin')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel_api.guest')),
            ],
        ),
    ]
