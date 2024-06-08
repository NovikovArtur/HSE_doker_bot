# Generated by Django 4.2.13 on 2024-06-06 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.CharField(max_length=255, unique=True, verbose_name='ID пользователя')),
                ('username', models.CharField(blank=True, max_length=32, null=True, verbose_name='Юзернейм пользователя')),
                ('timezone', models.IntegerField(blank=True, null=True, verbose_name='Часовой пояс')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]