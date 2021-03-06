# Generated by Django 2.2.12 on 2020-04-15 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20200413_0856'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(default='enter description', max_length=250)),
                ('img', models.CharField(default='orders/images/dish1.png', max_length=100)),
                ('category', models.CharField(choices=[('pizza', 'pizza'), ('dinner platter', 'dinner_platter'), ('pasta', 'pasta'), ('salad', 'salad'), ('sub', 'sub')], max_length=20)),
                ('veg', models.BooleanField()),
                ('price', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_of_toppings', models.IntegerField()),
                ('menu_item', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='pizza', to='orders.MenuItem')),
                ('order_item', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='pizza', to='orders.OrderItem')),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='menu_item',
        ),
        migrations.AlterField(
            model_name='topping',
            name='pizza',
            field=models.ManyToManyField(blank=True, related_name='toppings', to='orders.Pizza'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='orders.Order'),
        ),
    ]
