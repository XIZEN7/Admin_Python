# Generated by Django 3.0.6 on 2020-06-24 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multimedia', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='file',
            options={'managed': False, 'verbose_name_plural': 'Archivos'},
        ),
        migrations.AlterModelOptions(
            name='filecategory',
            options={'managed': False, 'verbose_name_plural': 'Categoria de archivos'},
        ),
        migrations.AlterModelOptions(
            name='filevalidity',
            options={'managed': False, 'verbose_name_plural': 'Validacion de archivo'},
        ),
        migrations.AlterModelOptions(
            name='multimedia',
            options={'managed': False, 'verbose_name_plural': 'Multimedia'},
        ),
    ]
