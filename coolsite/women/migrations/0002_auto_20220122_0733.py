# Generated by Django 3.2.9 on 2022-01-22 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='women',
            options={'ordering': ['title'], 'verbose_name': 'Famous women', 'verbose_name_plural': 'Famous women'},
        ),
        migrations.AlterField(
            model_name='women',
            name='content',
            field=models.TextField(blank=True, verbose_name='Article text'),
        ),
    ]
