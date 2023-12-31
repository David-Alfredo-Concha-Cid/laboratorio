# Generated by Django 4.1.1 on 2023-07-19 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directorgeneral',
            name='laboratorio',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='laboratorio.laboratorio'),
        ),
        migrations.AlterField(
            model_name='directorgeneral',
            name='nombre',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='laboratorio',
            name='nombre',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='producto',
            name='laboratorio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='laboratorio.laboratorio'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
