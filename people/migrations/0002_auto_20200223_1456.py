# Generated by Django 2.0.6 on 2020-02-23 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'managed': False, 'verbose_name': '订单管理', 'verbose_name_plural': '订单管理'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'managed': False, 'verbose_name': '用户管理', 'verbose_name_plural': '用户管理'},
        ),
    ]