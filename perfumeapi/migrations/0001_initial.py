# Generated by Django 3.2.4 on 2021-06-25 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfumes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('familiaOlfativa', models.CharField(max_length=150)),
                ('marca', models.CharField(max_length=100)),
                ('volumetria', models.IntegerField()),
            ],
        ),
    ]