# Generated by Django 3.0.3 on 2020-07-22 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_name', models.CharField(max_length=264, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Webpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_name', models.CharField(max_length=264, unique=True)),
                ('url', models.URLField(unique=True)),
                ('top_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mtv_app.Topic')),
            ],
        ),
        migrations.CreateModel(
            name='AccessRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('web_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mtv_app.Webpage')),
            ],
        ),
    ]