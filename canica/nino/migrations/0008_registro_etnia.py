# Generated by Django 2.2 on 2019-10-08 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nino', '0007_nivel_nutricion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro_etnia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('estado', models.BooleanField(null=True)),
            ],
            options={
                'verbose_name': 'Registro_etnia',
                'verbose_name_plural': 'Registro_etnias',
            },
        ),
    ]
