# Generated by Django 2.2.3 on 2020-02-06 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20200205_0434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='item_changed_by',
        ),
        migrations.DeleteModel(
            name='HistoricalItem',
        ),
    ]
