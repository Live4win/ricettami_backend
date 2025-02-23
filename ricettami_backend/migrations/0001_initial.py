# Generated by Django 5.1.6 on 2025-02-14 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AICard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=150)),
                ('content', models.CharField(max_length=600)),
                ('card_id', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommunityCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=150)),
                ('content', models.CharField(max_length=600)),
                ('card_id', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=150)),
                ('content', models.CharField(max_length=600)),
                ('card_id', models.IntegerField(unique=True)),
            ],
        ),
    ]
