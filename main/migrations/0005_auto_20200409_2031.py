# Generated by Django 3.0.5 on 2020-04-09 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200409_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_imageurl',
            field=models.CharField(default='static/main/images/noimage.png', max_length=200),
        ),
    ]