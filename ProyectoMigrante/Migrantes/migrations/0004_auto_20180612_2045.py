# Generated by Django 2.0.4 on 2018-06-13 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Migrantes', '0003_perfilesdeusuario_tipo_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='perfilesdeusuario',
            name='tipo_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Migrantes.Tipo_Usuario'),
        ),
    ]
