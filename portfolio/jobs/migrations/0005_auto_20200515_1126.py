# Generated by Django 3.0.6 on 2020-05-15 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20200515_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='link',
            field=models.URLField(blank=True, default='https://github.com/ninjananjo/'),
        ),
    ]