# Generated by Django 2.0 on 2019-06-25 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0004_auto_20190625_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='pages',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
