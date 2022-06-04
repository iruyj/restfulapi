# Generated by Django 3.2.12 on 2022-06-04 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='해당날짜')),
                ('start', models.TimeField(auto_now_add=True, verbose_name='시작시간')),
                ('end', models.TimeField(null=True, verbose_name='완료시간')),
                ('stretch', models.IntegerField(verbose_name='해당스트레칭번호')),
                ('status', models.IntegerField(verbose_name='현재상태')),
                ('user_email', models.EmailField(default=False, max_length=254)),
            ],
            options={
                'verbose_name': '스트레칭 테이블',
                'db_table': 'cure',
                'ordering': ['created', 'start'],
            },
        ),
    ]
