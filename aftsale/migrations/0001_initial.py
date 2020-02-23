# Generated by Django 2.0.6 on 2020-02-18 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('partner', '0001_initial'),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('complaint_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('comname', models.CharField(default='匿名', max_length=20, null=True)),
                ('text', models.TextField()),
                ('reply_peoplr', models.CharField(max_length=20, null=True)),
                ('reply_text', models.TextField(null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('ticket_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partner.TicketInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluate',
            fields=[
                ('evaluate_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('reply_peoplr', models.CharField(max_length=20, null=True)),
                ('reply_text', models.TextField(null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Order')),
            ],
        ),
    ]