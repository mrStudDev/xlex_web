# Generated by Django 4.0 on 2022-07-29 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_sumulas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sumulas',
            name='sumula_materia',
            field=models.CharField(choices=[('Férias', 'Férias'), ('Contratos', 'Contratos'), ('ADI', 'ADI')], default='XLEX', max_length=100),
        ),
        migrations.AlterField(
            model_name='sumulas',
            name='sumula_tribunal',
            field=models.CharField(choices=[('STF', 'STF'), ('TST', 'TST'), ('STJ', 'STJ')], default='XLEX', max_length=100),
        ),
    ]