# Generated by Django 4.2.9 on 2024-06-07 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_notesmodel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='notesmodel',
            name='href_on_timer',
            field=models.TextField(blank=True, null=True, verbose_name='Ссылка на таймер'),
        ),
    ]