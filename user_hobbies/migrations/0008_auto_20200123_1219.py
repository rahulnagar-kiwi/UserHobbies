# Generated by Django 3.0.2 on 2020-01-23 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_hobbies', '0007_auto_20200123_0728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userhobby',
            name='hobby',
        ),
        migrations.AddField(
            model_name='userhobby',
            name='hobby',
            field=models.ManyToManyField(to='user_hobbies.Hobbies'),
        ),
    ]
