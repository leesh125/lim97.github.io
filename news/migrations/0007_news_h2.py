# Generated by Django 3.2.3 on 2021-06-17 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_remove_news_h2'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='h2',
            field=models.CharField(default=True, max_length=80),
        ),
    ]