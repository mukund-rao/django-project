# Generated by Django 2.0.5 on 2018-05-20 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mk', '0008_auto_20180520_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cust_id2',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='mk.Customer'),
        ),
    ]