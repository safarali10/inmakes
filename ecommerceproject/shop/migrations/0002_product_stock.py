# Generated by Django 4.2.3 on 2023-12-14 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=1223),
            preserve_default=False,
        ),
    ]
