# Generated by Django 3.1.1 on 2021-08-06 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=128)),
                ('autor', models.CharField(max_length=64)),
                ('sinopse', models.TextField()),
                ('data_publicacao', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='LivroVendaImagens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='anuncios')),
            ],
        ),
        migrations.CreateModel(
            name='LivroVenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalhes', models.JSONField(max_length=248)),
                ('preco', models.FloatField(max_length=64)),
                ('anunciante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('imagens', models.ManyToManyField(to='livros.LivroVendaImagens')),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='livros.livro')),
            ],
        ),
    ]