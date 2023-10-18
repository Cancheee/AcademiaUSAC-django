# Generated by Django 4.2.5 on 2023-10-17 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_curso', models.CharField(max_length=70, verbose_name='Nombre del Curso')),
                ('codigo', models.IntegerField(unique=True, verbose_name='Codigo')),
                ('horario', models.CharField(max_length=16, verbose_name='Horario')),
                ('costo', models.FloatField(verbose_name='Costo')),
                ('descripcion', models.CharField(max_length=300)),
                ('imagen', models.ImageField(upload_to='Cursos/')),
                ('cupo', models.IntegerField(default=0)),
                ('disponibilidad', models.BooleanField(verbose_name='Disponibilidad')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('catedratico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuarios.catedraticos', verbose_name='Catedratico')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
                'db_table': 'Cursos',
            },
        ),
    ]
