# Generated by Django 5.1.6 on 2025-02-27 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome Fantasia')),
                ('contato', models.CharField(max_length=20, verbose_name='Contato')),
                ('cnpj', models.CharField(max_length=150, verbose_name='CNPJ')),
                ('Email', models.CharField(max_length=200, verbose_name='E-mail')),
            ],
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='categoria'),
        ),
    ]
