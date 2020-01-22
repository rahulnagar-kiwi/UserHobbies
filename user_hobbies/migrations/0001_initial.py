# Generated by Django 3.0.2 on 2020-01-22 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hobbies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField()),
                ('about', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserHobby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('hobby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_hobbies.Hobbies')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_hobbies.User')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('honesty', models.IntegerField(verbose_name=range(0, 5))),
                ('hardwork', models.IntegerField(verbose_name=range(0, 5))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_hobbies.User')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('1', 'is_active'), ('2', 'deactivated')], default='1', max_length=20)),
                ('is_delete', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user_hobbies.User')),
            ],
        ),
    ]
