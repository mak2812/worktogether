# Generated by Django 3.0.5 on 2020-05-02 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200503_0037'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='institute',
            field=models.CharField(default='', max_length=200),
        ),
    ]
