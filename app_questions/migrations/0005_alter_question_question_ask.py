# Generated by Django 4.0 on 2022-07-28 19:37

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_questions', '0004_alter_question_materia_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_ask',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
