# Generated by Django 2.0.5 on 2018-05-13 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mk', '0005_auto_20180513_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocks',
            name='isin',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
    ]