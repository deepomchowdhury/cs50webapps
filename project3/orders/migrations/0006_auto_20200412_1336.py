# Generated by Django 3.0.5 on 2020-04-12 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200412_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dinnerplatter',
            name='large_price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='dinnerplatter',
            name='medium_price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='dinnerplatter',
            name='small_price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='large_price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='medium_price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='small_price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='sub',
            name='large_price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='sub',
            name='medium_price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='sub',
            name='small_price',
            field=models.FloatField(null=True),
        ),
    ]
