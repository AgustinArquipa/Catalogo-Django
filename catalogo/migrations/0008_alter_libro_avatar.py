# Generated by Django 4.1.3 on 2022-11-07 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0007_libro_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='avatar',
            field=models.FilePathField(path='fotos', verbose_name='foto'),
        ),
    ]
