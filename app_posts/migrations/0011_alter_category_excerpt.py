# Generated by Django 4.0 on 2022-07-28 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_posts', '0010_alter_postsxlex_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='excerpt',
            field=models.CharField(default='Uncategorizeted', max_length=150),
        ),
    ]
