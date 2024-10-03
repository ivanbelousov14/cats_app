# Generated by Django 5.1.1 on 2024-10-03 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats_show', '0007_cat_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='color',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='cat',
            name='gender',
            field=models.CharField(blank=True, choices=[('m', 'male'), ('f', 'female')], default='m', max_length=1),
        ),
    ]
