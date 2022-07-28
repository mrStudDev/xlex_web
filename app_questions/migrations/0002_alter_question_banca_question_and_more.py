# Generated by Django 4.0 on 2022-07-28 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='banca_question',
            field=models.CharField(choices=[('FGV', 'FGV'), ('VUNESP', 'VUNESP')], default='Undefined', max_length=255),
        ),
        migrations.AlterField(
            model_name='question',
            name='materia_question',
            field=models.CharField(choices=[('Direito Civil', 'Direito Civil'), ('Ética', 'Ética')], default='Undefined', max_length=255),
        ),
    ]
