# Generated by Django 2.1.4 on 2019-02-13 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pingtai', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='sh',
            field=models.IntegerField(choices=[(0, '未审核'), (1, '审核中'), (2, '审核通过')], default=1),
        ),
    ]