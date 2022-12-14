# Generated by Django 4.1.1 on 2022-11-01 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0023_principle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=True, max_length=30)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.IntegerField(blank=True, default=0, null=True)),
                ('suggest', models.TextField(blank=True, default='')),
            ],
        ),
    ]
