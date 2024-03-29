# Generated by Django 2.2.5 on 2019-09-30 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comentarios', '0001_initial'),
        ('recursos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PontoTuristico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('descricao', models.TextField()),
                ('aprovado', models.BooleanField(default=False)),
                ('comentarios', models.ManyToManyField(to='comentarios.Comentario')),
                ('recursos', models.ManyToManyField(to='recursos.Recurso')),
            ],
        ),
    ]
