# Generated by Django 2.1.5 on 2019-01-31 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20190130_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='almacen',
            field=models.DecimalField(decimal_places=0, max_digits=100),
        ),
    ]