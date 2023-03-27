# Generated by Django 3.2.9 on 2023-03-27 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0006_xarajatlar_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hodim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('oname', models.CharField(max_length=20)),
                ('jshir', models.CharField(max_length=14)),
                ('pasport', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='IshxaqiXarajati',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summa', models.FloatField()),
                ('comment', models.TextField()),
                ('hodim', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='homes.hodim')),
            ],
        ),
    ]
