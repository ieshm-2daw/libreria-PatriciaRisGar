# Generated by Django 3.2.23 on 2023-12-12 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0004_auto_20231130_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='cover/'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='returnDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
