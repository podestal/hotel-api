# Generated by Django 5.0 on 2023-12-23 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_api', '0002_remove_cabin_description_remove_cabin_discount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creted_at', models.DateTimeField(auto_now=True)),
                ('text', models.CharField(max_length=255)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
