# Generated by Django 2.0.5 on 2018-05-13 13:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mk', '0003_auto_20180513_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='username',
            field=models.OneToOneField(max_length=15, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
