# Generated by Django 4.1.1 on 2022-10-11 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0016_tutorial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('informations', models.TextField(blank=True, null=True)),
            ],
        ),
    ]