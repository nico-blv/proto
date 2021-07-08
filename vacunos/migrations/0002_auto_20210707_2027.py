# Generated by Django 3.2.5 on 2021-07-08 00:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vacunos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lote',
            name='cantVacuno',
            field=models.IntegerField(default=1, verbose_name='Cantidad de vacuno'),
        ),
        migrations.AddField(
            model_name='lote',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lote',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
