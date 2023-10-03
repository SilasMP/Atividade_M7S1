# Generated by Django 4.2.4 on 2023-10-03 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('descricao', models.CharField(max_length=300, verbose_name='Descrição')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
