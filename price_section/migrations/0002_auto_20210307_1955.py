# Generated by Django 3.1.7 on 2021-03-07 19:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('price_section', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='crypto',
            options={'ordering': ['created_at']},
        ),
        migrations.AddField(
            model_name='crypto',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]