# Generated by Django 2.0.4 on 2018-04-27 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cursos', '0019_auto_20180422_2255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preguntas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('cuerpo', models.TextField(max_length=300)),
                ('respuesta', models.TextField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='descripcion',
            field=models.TextField(default='', max_length=300),
        ),
    ]
