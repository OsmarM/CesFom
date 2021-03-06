# Generated by Django 2.0.3 on 2018-04-13 23:20

from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Cursos', '0008_auto_20180413_1610'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContenidoTema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', embed_video.fields.EmbedVideoField()),
            ],
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tema', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='unidad',
            name='video',
        ),
        migrations.AddField(
            model_name='unidad',
            name='curso',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Cursos.Course'),
        ),
        migrations.AddField(
            model_name='unidad',
            name='descripcion',
            field=models.TextField(default='', max_length=240),
        ),
        migrations.AlterField(
            model_name='unidad',
            name='nombre_unidad',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='unidad',
            name='numero_unidad',
            field=models.IntegerField(default=''),
        ),
        migrations.AddField(
            model_name='tema',
            name='unidad',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Cursos.Unidad'),
        ),
        migrations.AddField(
            model_name='contenidotema',
            name='titulo',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Cursos.Tema'),
        ),
    ]
