# Generated by Django 4.0 on 2022-07-26 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postsxlex',
            name='category',
            field=models.CharField(default='XLEX', max_length=100),
        ),
    ]
