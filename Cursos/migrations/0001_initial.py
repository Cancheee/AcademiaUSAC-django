# Generated by Django 4.2.5 on 2023-10-19 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Asignacion',
                'verbose_name_plural': 'Asignaciones',
                'db_table': 'Asignaciones',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70, verbose_name='Nombre del Curso')),
                ('codigo', models.IntegerField(unique=True, verbose_name='Codigo')),
                ('horario', models.CharField(max_length=16, verbose_name='Horario')),
                ('precio', models.FloatField(verbose_name='Precio')),
                ('descripcion', models.CharField(max_length=300)),
                ('imagen', models.ImageField(upload_to='Cursos/')),
                ('cupo_limite', models.PositiveIntegerField()),
                ('cupo_actual', models.PositiveIntegerField(default=0)),
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
        migrations.CreateModel(
            name='LineaAsignacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cupo', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('asignacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cursos.asignaciones')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cursos.cursos')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'LineaAsignacion',
                'verbose_name_plural': 'LineaAsignaciones',
                'db_table': 'LineaAsignaciones',
                'ordering': ['id'],
            },
        ),
    ]
