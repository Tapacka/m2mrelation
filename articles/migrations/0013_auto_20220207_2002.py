# Generated by Django 3.1.2 on 2022-02-07 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_article_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tags',
            options={'ordering': ['name'], 'verbose_name': 'Тэг', 'verbose_name_plural': 'Тэги'},
        ),
    ]
