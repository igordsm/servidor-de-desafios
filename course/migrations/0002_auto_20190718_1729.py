# Generated by Django 2.1.7 on 2019-07-18 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0006_challengesubmission_errors'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChallengeBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1024)),
                ('release_date', models.DateTimeField(blank=True, null=True, verbose_name='release date')),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='date ended'),
        ),
        migrations.AddField(
            model_name='class',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='date started'),
        ),
        migrations.AddField(
            model_name='challengeblock',
            name='block_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Class'),
        ),
        migrations.AddField(
            model_name='challengeblock',
            name='challenges',
            field=models.ManyToManyField(to='challenges.Challenge'),
        ),
    ]
