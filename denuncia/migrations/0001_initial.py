# Generated by Django 4.2.11 on 2025-03-27 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Denuncia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome completo')),
                ('cpf', models.CharField(max_length=255, verbose_name='CPF')),
                ('endereco', models.TextField(max_length=255, verbose_name='Endereço completo')),
                ('descricao', models.CharField(max_length=255, verbose_name='Descricao')),
                ('celular', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nome completo')),
                ('status_denuncia', models.CharField(choices=[(1, 'Em análise'), (2, 'Arquivada'), (3, 'Concluida')], max_length=255, verbose_name='Status')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
