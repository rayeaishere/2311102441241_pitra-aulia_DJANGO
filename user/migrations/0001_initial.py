# Generated by Django 5.1.7 on 2025-03-14 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Biodata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alamat', models.TextField(blank=True, null=True)),
                ('telepon', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
