# Generated by Django 2.0.4 on 2018-06-14 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Migrantes', '0005_auto_20180613_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilesdeusuario',
            name='tipo',
            field=models.CharField(default='Estudiante', max_length=40),
        ),
    ]
