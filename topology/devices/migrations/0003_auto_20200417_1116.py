# Generated by Django 3.0.5 on 2020-04-17 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0002_auto_20200417_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='switch',
            name='ip',
            field=models.GenericIPAddressField(unique=True),
        ),
        migrations.AlterField(
            model_name='switch',
            name='mac_address',
            field=models.CharField(blank=True, max_length=17, null=True, unique=True),
        ),
    ]
