# Generated by Django 4.1.5 on 2023-02-23 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btsweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='btsuser',
            name='usercode',
            field=models.CharField(max_length=6, null=True),
        ),
    ]
