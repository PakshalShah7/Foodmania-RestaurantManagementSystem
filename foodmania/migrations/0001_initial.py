# Generated by Django 4.1.1 on 2023-04-06 14:08

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False,
                                           verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(
                    auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(
                    auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False,
                                           verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(
                    auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(
                    auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=150)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(default='food_images/default_food.jpg',
                                            upload_to='food_images/')),
                ('stock', models.IntegerField(default=50)),
                ('status', models.CharField(choices=[('Disabled', 'Disabled'),
                                                     ('Enabled', 'Enabled')],
                                            default='Enabled', max_length=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                               related_name='food_items',
                                               to='foodmania.category')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
