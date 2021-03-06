# Generated by Django 2.2.13 on 2020-10-17 15:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backManage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='admin_verification',
            field=models.CharField(default='否', max_length=10, verbose_name='管理员是否审核通过'),
        ),
        migrations.AlterField(
            model_name='college',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 17, 15, 36, 19, 683035, tzinfo=utc), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 17, 15, 36, 19, 683035, tzinfo=utc), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='judge',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 17, 15, 36, 19, 687251, tzinfo=utc), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='member',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 17, 15, 36, 19, 684089, tzinfo=utc), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='team',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 17, 15, 36, 19, 685149, tzinfo=utc), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='work',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 17, 15, 36, 19, 686200, tzinfo=utc)),
        ),
    ]
