# Generated by Django 3.2.25 on 2024-06-03 14:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20240603_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='articoli',
            name='autore',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='articoli',
            name='stato',
            field=models.CharField(choices=[('BZ', 'Bozza'), ('PB', 'Pubblicato'), ('RV', 'Revisione')], default='BZ', max_length=2),
        ),
    ]