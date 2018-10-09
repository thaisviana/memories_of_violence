# Generated by Django 2.1.2 on 2018-10-09 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('occurrence', '0004_occurrence_location'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asset',
            options={'verbose_name': 'Material', 'verbose_name_plural': 'Materiais'},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name': 'Localização', 'verbose_name_plural': 'Localizações'},
        ),
        migrations.AlterModelOptions(
            name='occurrence',
            options={'verbose_name': 'Ocorrência', 'verbose_name_plural': 'Ocorrências'},
        ),
        migrations.AddField(
            model_name='asset',
            name='occurrence',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='occurrence.Occurrence'),
        ),
    ]