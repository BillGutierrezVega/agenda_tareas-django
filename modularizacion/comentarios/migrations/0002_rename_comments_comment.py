# Generated by Django 4.1.7 on 2023-11-20 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='comments',
            new_name='Comment',
        ),
    ]