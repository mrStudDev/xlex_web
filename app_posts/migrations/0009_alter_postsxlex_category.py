# Generated by Django 4.0 on 2022-07-26 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_posts', '0008_alter_postsxlex_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postsxlex',
            name='category',
            field=models.CharField(choices=[], default='XLEX', max_length=100),
        ),
    ]