# Generated by Django 4.1.1 on 2022-10-11 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0017_inform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inform',
            name='informations',
        ),
        migrations.AddField(
            model_name='inform',
            name='i',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]