# Generated by Django 4.2.5 on 2023-10-10 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0015_alter_cast_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cast',
            name='movie',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='films.movie'),
        ),
    ]
