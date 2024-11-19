# Generated by Django 5.1.2 on 2024-11-19 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_egliseinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evenement',
            old_name='date',
            new_name='date_debut',
        ),
        migrations.AddField(
            model_name='evenement',
            name='date_fin',
            field=models.CharField(default='Non précisé', max_length=50),
        ),
        migrations.AddField(
            model_name='evenement',
            name='lieu',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
