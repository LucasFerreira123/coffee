# Generated by Django 5.0.2 on 2024-02-21 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='receita',
            name='ingredientes',
        ),
        migrations.RemoveField(
            model_name='receita',
            name='autor',
        ),
        migrations.DeleteModel(
            name='Ingrediente',
        ),
        migrations.DeleteModel(
            name='Receita',
        ),
    ]
