# Generated by Django 3.2.5 on 2021-09-14 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_carrinho_loja'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='disponivel',
            field=models.BooleanField(default=True),
        ),
    ]