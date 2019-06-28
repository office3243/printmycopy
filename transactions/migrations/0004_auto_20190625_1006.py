# Generated by Django 2.0 on 2019-06-25 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_remove_transaction_reference1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='pages',
        ),
        migrations.AddField(
            model_name='file',
            name='pages',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
