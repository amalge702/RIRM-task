# Generated by Django 3.2 on 2021-04-14 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=30)),
                ('URL', models.URLField()),
                ('phone_number', models.CharField(max_length=12)),
            ],
        ),
    ]
