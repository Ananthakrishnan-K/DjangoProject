# Generated by Django 3.0.5 on 2020-04-24 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='customer_name',
            field=models.CharField(default='Company Name', max_length=50),
        ),
    ]
