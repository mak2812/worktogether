# Generated by Django 3.0.5 on 2020-05-01 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grp', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='grpname',
            field=models.CharField(default='TECAPP', max_length=100),
        ),
    ]
