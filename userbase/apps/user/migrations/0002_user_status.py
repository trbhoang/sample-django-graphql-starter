# Generated by Django 3.2.3 on 2021-05-18 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(default='REGISTERED', max_length=50),
        ),
    ]
