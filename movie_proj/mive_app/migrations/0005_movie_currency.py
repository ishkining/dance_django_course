# Generated by Django 4.1.6 on 2023-02-08 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mive_app', '0004_alter_movie_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='currency',
            field=models.CharField(choices=[('E', 'Euro'), ('D', 'Dollars'), ('R', 'Rubles')], default='R', max_length=1),
        ),
    ]
