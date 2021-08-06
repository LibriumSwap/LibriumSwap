# Generated by Django 3.1.1 on 2021-08-06 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnderecoUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_user', models.CharField(max_length=128)),
                ('cpf', models.CharField(max_length=11)),
                ('contato', models.CharField(max_length=11)),
                ('cep', models.CharField(max_length=8)),
                ('estado', models.CharField(max_length=64)),
                ('cidade', models.CharField(max_length=64)),
                ('rua', models.CharField(max_length=128)),
                ('complemento', models.CharField(max_length=128)),
                ('numero', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_funcionario',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='enderecos',
            field=models.ManyToManyField(to='autenticacao.EnderecoUser'),
        ),
    ]
