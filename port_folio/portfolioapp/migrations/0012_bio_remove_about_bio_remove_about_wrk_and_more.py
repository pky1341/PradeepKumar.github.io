# Generated by Django 4.1.1 on 2022-10-05 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0011_alter_about_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(default='', null=True)),
                ('wrk', models.TextField(default='', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='about',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='about',
            name='wrk',
        ),
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(upload_to='personal'),
        ),
    ]
