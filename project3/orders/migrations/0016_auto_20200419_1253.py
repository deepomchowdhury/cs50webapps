# Generated by Django 2.2.12 on 2020-04-19 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_auto_20200417_0658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='completed',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('completed', 'completed'), ('not completed', 'not completed'), ('cancelled', 'cancelled')], default='not completed', max_length=20),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='order_item', to='orders.Order'),
        ),
    ]
