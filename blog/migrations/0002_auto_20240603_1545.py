# Generated by Django 3.2.25 on 2024-06-03 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articoli',
            options={'verbose_name_plural': 'Articoli'},
        ),
        migrations.AddField(
            model_name='articoli',
            name='stato',
            field=models.CharField(choices=[('BZ', 'Bozza'), ('PB', 'Pubblicato')], default='BZ', max_length=2),
        ),
    ]