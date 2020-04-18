# Generated by Django 3.0.5 on 2020-04-17 19:35

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aps',
            fields=[
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('ap', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='AP')),
                ('modelo', models.CharField(max_length=80, verbose_name='Modelo')),
                ('canal', models.IntegerField(verbose_name='Canal')),
                ('image', stdimage.models.StdImageField(upload_to='aps', verbose_name='Imagem')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=100, verbose_name='Slug')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
