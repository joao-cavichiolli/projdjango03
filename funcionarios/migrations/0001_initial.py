# Generated by Django 4.0.2 on 2022-02-14 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.IntegerField()),
                ('sexo', models.CharField(max_length=1)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
