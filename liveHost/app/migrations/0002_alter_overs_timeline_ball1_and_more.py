# Generated by Django 5.0.6 on 2024-06-07 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overs_timeline',
            name='ball1',
            field=models.CharField(db_default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='overs_timeline',
            name='ball2',
            field=models.CharField(db_default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='overs_timeline',
            name='ball3',
            field=models.CharField(db_default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='overs_timeline',
            name='ball4',
            field=models.CharField(db_default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='overs_timeline',
            name='ball5',
            field=models.CharField(db_default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='overs_timeline',
            name='ball6',
            field=models.CharField(db_default='', max_length=250),
        ),
    ]
