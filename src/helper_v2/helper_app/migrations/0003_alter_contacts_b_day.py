# Generated by Django 4.0.10 on 2023-04-09 16:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helper_app', '0002_alter_contacts_b_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='b_day',
            field=models.DateField(default=datetime.date(2023, 4, 9), null=True),
        ),
    ]
