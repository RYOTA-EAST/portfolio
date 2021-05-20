# Generated by Django 3.2 on 2021-05-19 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_work_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='genre',
            field=models.CharField(choices=[('0', 'フロントエンド'), ('1', 'バックエンド'), ('2', 'デプロイ'), ('3', 'その他')], default='', max_length=1, verbose_name='ジャンル'),
        ),
    ]