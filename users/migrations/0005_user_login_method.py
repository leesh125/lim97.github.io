# Generated by Django 3.2.3 on 2021-05-27 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210524_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='login_method',
            field=models.CharField(choices=[('email', 'Email'), ('kakao', 'Kakao')], default='email', max_length=50),
        ),
    ]
