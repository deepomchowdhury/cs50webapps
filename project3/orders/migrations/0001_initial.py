# Generated by Django 2.0.3 on 2020-04-11 09:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DinnerPlatter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('small_price', models.IntegerField(null=True)),
                ('medium_price', models.IntegerField(null=True)),
                ('large_price', models.IntegerField(null=True)),
                ('size', models.CharField(choices=[('small', 'small'), ('medium', 'medium'), ('large', 'large')], default='small', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('description', models.CharField(max_length=250)),
                ('category', models.CharField(choices=[('pizza', 'pizza'), ('dinner platter', 'dinner_platter'), ('pasta', 'pasta'), ('salad', 'salad')], max_length=20)),
                ('veg', models.BooleanField()),
                ('price', models.IntegerField()),
                ('menu', models.ManyToManyField(blank=True, related_name='menu_items', to='orders.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('price', models.IntegerField()),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='orders.MenuItem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_type', models.CharField(max_length=64, unique=True)),
                ('small_price', models.IntegerField(null=True)),
                ('medium_price', models.IntegerField(null=True)),
                ('large_price', models.IntegerField(null=True)),
                ('size', models.CharField(choices=[('small', 'small'), ('medium', 'medium'), ('large', 'large')], default='small', max_length=10)),
                ('subs', models.IntegerField(null=True)),
                ('toppings', models.IntegerField(null=True)),
                ('menu_item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pizza', to='orders.MenuItem')),
            ],
        ),
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('small_price', models.IntegerField(null=True)),
                ('medium_price', models.IntegerField(null=True)),
                ('large_price', models.IntegerField(null=True)),
                ('size', models.CharField(choices=[('small', 'small'), ('medium', 'medium'), ('large', 'large')], default='small', max_length=10)),
                ('pizza', models.ManyToManyField(blank=True, to='orders.Pizza')),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('price', models.IntegerField()),
                ('pizza', models.ManyToManyField(blank=True, to='orders.Pizza')),
            ],
        ),
        migrations.AddField(
            model_name='dinnerplatter',
            name='menu_item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='dinner_platter', to='orders.MenuItem'),
        ),
    ]
