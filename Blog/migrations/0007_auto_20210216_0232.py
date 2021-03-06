# Generated by Django 3.1.6 on 2021-02-16 02:32

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_auto_20210211_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categoria',
            field=models.CharField(choices=[('defi', 'Defi'), ('trading', 'Trading'), ('noticias', 'Noticias'), ('blockchain', 'Blockchain'), ('educacion', 'Educacion')], default='Noticias', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
