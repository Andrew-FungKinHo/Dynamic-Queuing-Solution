# Generated by Django 3.2 on 2021-04-15 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerview', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('currentLocation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('profilePic', models.URLField(null=True)),
                ('numberOfLikes', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderType', models.CharField(choices=[('Dine In', 'Dine-in'), ('Takeaway', 'Take-away'), ('Delivery', 'Delivery')], max_length=8)),
                ('totalPrice', models.FloatField(null=True)),
                ('startTime', models.DateField(max_length=20)),
                ('endTime', models.DateField(max_length=20)),
            ],
        ),
    ]
