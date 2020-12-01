# Generated by Django 3.0.5 on 2020-11-17 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=30)),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=15)),
                ('phoneNumber', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=15)),
                ('entryPoints', models.CharField(max_length=15)),
            ],
        ),
    ]