# Generated by Django 4.1.1 on 2023-04-12 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodmania', '0002_alter_category_options_alter_food_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='food',
            options={'ordering': ['id']},
        ),
    ]
