# Generated by Django 5.0.1 on 2024-01-20 17:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_question_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 20, 17, 6, 18, 115180, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
    ]
