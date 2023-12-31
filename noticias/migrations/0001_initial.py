# Generated by Django 4.2.4 on 2023-10-03 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0003_alter_categorias_nome'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('titulo', models.CharField(max_length=300, verbose_name='Título')),
                ('descricao', models.TextField(verbose_name='Escreva o texto da Noticia aqui:')),
                ('categoria', models.ForeignKey(default='Noticia', on_delete=django.db.models.deletion.SET_DEFAULT, to='base.categorias')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
