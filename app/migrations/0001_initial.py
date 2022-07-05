# Generated by Django 4.0.6 on 2022-07-05 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('typeOne', models.CharField(max_length=30)),
                ('typeTwo', models.CharField(max_length=30)),
                ('hp', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('spattack', models.IntegerField()),
                ('spdefense', models.IntegerField()),
                ('speed', models.IntegerField()),
            ],
        ),
    ]
