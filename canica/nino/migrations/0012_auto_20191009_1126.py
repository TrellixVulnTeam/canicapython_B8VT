# Generated by Django 2.0.13 on 2019-10-09 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nino', '0011_auto_20191008_1856'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area_Dental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnostico', models.TextField()),
                ('intervencion', models.TextField()),
                ('proxima_cita', models.DateField()),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Area_Dental',
                'verbose_name_plural': 'Area_Dentals',
            },
        ),
        migrations.CreateModel(
            name='Area_Medica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.IntegerField()),
                ('altura', models.FloatField()),
                ('presencia_piojos', models.BooleanField()),
                ('presencia_acaros', models.BooleanField()),
                ('programa_vacunacion', models.BooleanField()),
                ('examen_sangre', models.BooleanField()),
                ('examne_orina', models.BooleanField()),
                ('estado_piel', models.TextField()),
            ],
            options={
                'verbose_name': 'Area_Medica',
                'verbose_name_plural': 'Area_Medicas',
            },
        ),
        migrations.CreateModel(
            name='Area_Psicologica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_emocional', models.TextField(null=True)),
                ('aspecto_clinico', models.TextField(null=True)),
                ('percepcion_situacion_desproteccion', models.BooleanField()),
                ('percepcion_calidad_vida', models.BooleanField()),
                ('percepcion_temores_actuales', models.TextField(null=True)),
                ('percepcion_temores_futuros', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'Area_Psicologica',
                'verbose_name_plural': 'Area_Psicologicas',
            },
        ),
        migrations.CreateModel(
            name='Area_Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol_familiar', models.TextField(null=True)),
                ('visitas_autorizadas', models.BooleanField()),
                ('recurso_familiar', models.CharField(max_length=60, null=True)),
            ],
            options={
                'verbose_name': 'Area_Social',
                'verbose_name_plural': 'Area_Socials',
            },
        ),
        migrations.CreateModel(
            name='Enfermedad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_enfermedad', models.CharField(max_length=60)),
                ('descripcion', models.TextField()),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Enfermedad',
                'verbose_name_plural': 'Enfermedads',
            },
        ),
        migrations.CreateModel(
            name='Etnia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_etnia', models.CharField(max_length=60)),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Etnia',
                'verbose_name_plural': 'Etnias',
            },
        ),
        migrations.CreateModel(
            name='Fuente_Estre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_fuente', models.CharField(max_length=60)),
                ('descripcion', models.TextField()),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Fuente_Estre',
                'verbose_name_plural': 'Fuente_Estres',
            },
        ),
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_idioma', models.CharField(max_length=60)),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Idioma',
                'verbose_name_plural': 'Idiomas',
            },
        ),
        migrations.CreateModel(
            name='Nino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_evaluacion', models.DateField()),
                ('nombre_nino', models.CharField(max_length=60)),
                ('apellido_nino', models.CharField(max_length=60)),
                ('image', models.ImageField(upload_to='img')),
                ('cui', models.CharField(max_length=60)),
                ('sexo', models.CharField(max_length=3)),
                ('grado_educativo', models.CharField(max_length=30, null=True)),
                ('fecha_nacimiento', models.DateField()),
                ('lugar_nacimiento', models.CharField(max_length=60)),
                ('lugar_residencia', models.CharField(max_length=60)),
                ('ocupacion', models.CharField(max_length=60, null=True)),
                ('religion', models.CharField(max_length=30, null=True)),
                ('nombre_madre', models.CharField(max_length=100)),
                ('nombre_padre', models.CharField(max_length=100)),
                ('fecha_ingreso', models.DateField()),
                ('estado', models.BooleanField(default=True)),
                ('etnia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nino.Etnia')),
                ('idioma', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nino.Idioma')),
            ],
            options={
                'verbose_name': 'Nino',
                'verbose_name_plural': 'Ninos',
            },
        ),
        migrations.CreateModel(
            name='Relacion_Familia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_relacion', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Relacion_Familia',
                'verbose_name_plural': 'Relacion_Familias',
            },
        ),
        migrations.DeleteModel(
            name='Registro_Enfermedade',
        ),
        migrations.DeleteModel(
            name='Registro_etnia',
        ),
        migrations.DeleteModel(
            name='Registro_Idioma',
        ),
        migrations.AlterModelOptions(
            name='nivel_nutricion',
            options={'verbose_name': 'Nivel_Nutricion', 'verbose_name_plural': 'Nivel_Nutricions'},
        ),
        migrations.RemoveField(
            model_name='motivo_ingreso',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='nivel_nutricion',
            name='nombre',
        ),
        migrations.AddField(
            model_name='motivo_ingreso',
            name='descripcion',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='motivo_ingreso',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='motivo_ingreso',
            name='nombre_motivo',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nivel_nutricion',
            name='descripcion',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nivel_nutricion',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='nivel_nutricion',
            name='nivel',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nino',
            name='motivo_ingreso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nino.Motivo_Ingreso'),
        ),
        migrations.AddField(
            model_name='area_social',
            name='fuente_estres',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nino.Fuente_Estre'),
        ),
        migrations.AddField(
            model_name='area_social',
            name='nino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nino.Nino'),
        ),
        migrations.AddField(
            model_name='area_social',
            name='relacion_familiar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nino.Relacion_Familia'),
        ),
        migrations.AddField(
            model_name='area_psicologica',
            name='enfermedad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nino.Enfermedad'),
        ),
        migrations.AddField(
            model_name='area_psicologica',
            name='nino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nino.Nino'),
        ),
        migrations.AddField(
            model_name='area_medica',
            name='nino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nino.Nino'),
        ),
        migrations.AddField(
            model_name='area_medica',
            name='nivel_nutricion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nino.Nivel_Nutricion'),
        ),
        migrations.AddField(
            model_name='area_dental',
            name='nino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nino.Nino'),
        ),
    ]