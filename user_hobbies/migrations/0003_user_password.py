# Generated by Django 3.0.2 on 2020-01-22 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_hobbies', '0002_auto_20200122_0701'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
