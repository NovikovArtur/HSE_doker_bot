# Generated by Django 4.2.13 on 2024-06-06 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_notesmodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notesmodel',
            name='user',
            field=models.CharField(max_length=255, verbose_name='ID пользователя'),
        ),
    ]