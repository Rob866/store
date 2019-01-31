# Generated by Django 2.1.5 on 2019-01-31 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='almacen',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='disponibilidad',
            field=models.BooleanField(default=False),
        ),
    ]