# Generated by Django 3.2.5 on 2021-08-19 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_loja_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrinho',
            name='cliente',
        ),
    ]