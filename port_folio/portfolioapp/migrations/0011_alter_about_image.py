# Generated by Django 4.1.1 on 2022-10-05 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0010_about_bio_about_wrk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='personal'),
        ),
    ]
