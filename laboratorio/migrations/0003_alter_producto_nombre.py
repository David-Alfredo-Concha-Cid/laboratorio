# Generated by Django 4.1.1 on 2023-07-19 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0002_alter_directorgeneral_laboratorio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]
