# Generated by Django 4.0 on 2022-07-26 20:50

import app_posts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_posts', '0007_alter_postsxlex_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postsxlex',
            name='category',
            field=models.CharField(choices=[('TST', 'TST'), ('STJ', 'STJ'), ('Suprema Corte', 'Suprema Corte'), ('News', 'News'), ('International Laws', 'International Laws')], default='XLEX', max_length=100, verbose_name=app_posts.models.Category),
        ),
    ]
