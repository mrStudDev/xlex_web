# Generated by Django 4.0 on 2022-07-27 04:41

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_casos', '0003_alter_casoconcreto_lei_caso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casoconcreto',
            name='lei_caso',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
