# Generated by Django 4.1.3 on 2022-11-07 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0005_alter_libro_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='avatar',
        ),
    ]
