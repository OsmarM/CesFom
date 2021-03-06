# Generated by Django 2.0.3 on 2018-04-16 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cursos', '0009_auto_20180413_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Cursos.ContenidoTema')),
                ('curso', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Cursos.Course')),
                ('tema', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Cursos.Tema')),
                ('unidad', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Cursos.Unidad')),
            ],
        ),
    ]
