# Generated by Django 4.1.3 on 2022-11-16 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0013_alter_libro_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='foto',
            field=models.ImageField(null=True, upload_to='upload/'),
        ),
    ]