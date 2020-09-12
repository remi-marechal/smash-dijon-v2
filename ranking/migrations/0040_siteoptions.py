# Generated by Django 2.2.4 on 2020-09-05 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0039_auto_20200901_1748'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_name', models.CharField(max_length=255)),
                ('is_option_active', models.BooleanField(default=False, verbose_name='Système Actif')),
                ('is_inscription_open', models.BooleanField(default=False, verbose_name='Inscriptions Ouverte')),
            ],
        ),
    ]
