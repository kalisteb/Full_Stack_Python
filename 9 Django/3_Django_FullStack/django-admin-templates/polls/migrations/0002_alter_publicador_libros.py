# Generated by Django 3.2.6 on 2021-09-07 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicador',
            name='libros',
            field=models.ManyToManyField(related_name='publicadores', to='polls.Libro'),
        ),
    ]
