# Generated by Django 2.2.3 on 2020-01-31 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200130_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='bin',
            name='bin_last_edited_by',
            field=models.CharField(default='regent', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='card_last_edited_by',
            field=models.CharField(default='regent', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='item_last_edited_by',
            field=models.CharField(default='regent', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='key',
            name='key_last_edited_by',
            field=models.CharField(default='regent', max_length=30),
            preserve_default=False,
        ),
    ]