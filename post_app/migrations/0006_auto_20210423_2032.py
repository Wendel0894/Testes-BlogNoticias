# Generated by Django 3.1.7 on 2021-04-23 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0005_auto_20210423_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
