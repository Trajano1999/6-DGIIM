# Generated by Django 4.1.1 on 2022-11-05 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='foto',
            field=models.FileField(upload_to='recetas/media/fotos'),
        ),
    ]