# Generated by Django 3.1.4 on 2021-04-16 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Age', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Adress', models.CharField(max_length=100)),
            ],
        ),
    ]
