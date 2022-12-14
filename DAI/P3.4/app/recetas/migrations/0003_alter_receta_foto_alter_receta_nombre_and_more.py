# Generated by Django 4.1.1 on 2022-11-28 14:51

from django.db import migrations, models
import recetas.models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0002_alter_receta_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='foto',
            field=models.FileField(upload_to='media/fotos'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='nombre',
            field=models.CharField(max_length=200, validators=[recetas.models.validate_mayus]),
        ),
        migrations.AlterField(
            model_name='receta',
            name='preparación',
            field=models.TextField(max_length=5000, validators=[recetas.models.validate_mayus]),
        ),
    ]
