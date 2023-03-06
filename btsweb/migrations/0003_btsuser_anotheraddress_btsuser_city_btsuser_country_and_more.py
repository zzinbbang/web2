# Generated by Django 4.1.5 on 2023-03-06 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btsweb', '0002_btsuser_usercode'),
    ]

    operations = [
        migrations.AddField(
            model_name='btsuser',
            name='anotheraddress',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='btsuser',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='btsuser',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='btsuser',
            name='password',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='btsuser',
            name='zip',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='btsuser',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='btsuser',
            name='fname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='btsuser',
            name='lname',
            field=models.CharField(max_length=50, null=True),
        ),
    ]