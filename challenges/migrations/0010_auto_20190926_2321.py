# Generated by Django 2.1.7 on 2019-09-27 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0009_prova'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prova',
            old_name='title',
            new_name='titulo',
        ),
    ]
