# Generated by Django 3.2.9 on 2023-03-21 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0003_xarajatlar_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='xarajatlar',
            name='date',
            field=models.DateField(),
        ),
        migrations.AddField(
            model_name='xarajatlar',
            name='manba',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='homes.bank'),
        ),
    ]
