# Generated by Django 4.0.4 on 2022-05-21 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=11)),
                ('neighborhood', models.CharField(max_length=60)),
                ('number', models.IntegerField()),
                ('district', models.CharField(max_length=30)),
                ('complement', models.CharField(blank=True, max_length=100)),
                ('zip_code', models.CharField(max_length=8)),
                ('state', models.CharField(max_length=2)),
                ('city', models.CharField(max_length=30)),
                ('cod_ibge', models.IntegerField()),
                ('photo_user', models.ImageField(upload_to='')),
            ],
        ),
    ]
