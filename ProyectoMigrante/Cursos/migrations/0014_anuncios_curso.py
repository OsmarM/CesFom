# Generated by Django 2.0.3 on 2018-04-22 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cursos', '0013_course_estudiante'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncios',
            name='curso',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Cursos.Course'),
        ),
    ]
