# Generated by Django 2.2 on 2019-11-08 11:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publicationDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]