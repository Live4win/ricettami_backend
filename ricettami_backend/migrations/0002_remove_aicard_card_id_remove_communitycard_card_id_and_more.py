# Generated by Django 5.1.6 on 2025-02-14 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ricettami_backend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aicard',
            name='card_id',
        ),
        migrations.RemoveField(
            model_name='communitycard',
            name='card_id',
        ),
        migrations.RemoveField(
            model_name='personalcard',
            name='card_id',
        ),
    ]
