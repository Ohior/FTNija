# Generated by Django 4.0.5 on 2022-06-29 01:46

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DictModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=200)),
                ('json', jsonfield.fields.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Dicty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='KeyVal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=200)),
                ('value', models.CharField(db_index=True, max_length=200)),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ftbot.dicty')),
            ],
        ),
    ]
