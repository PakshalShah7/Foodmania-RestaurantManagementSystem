# Generated by Django 4.1.1 on 2023-04-07 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodmania_website', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
