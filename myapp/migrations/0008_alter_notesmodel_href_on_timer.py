# Generated by Django 4.2.13 on 2024-06-07 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_notesmodel_href_on_timer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notesmodel',
            name='href_on_timer',
            field=models.TextField(blank=True, null=True, verbose_name='Ссылка на таймер'),
        ),
    ]
