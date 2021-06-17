# Generated by Django 3.2.3 on 2021-06-09 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0010_auto_20210604_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='channeltype',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='channeltype', to='channel.channeltype'),
        ),
        migrations.AlterField(
            model_name='channelimg',
            name='channel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chimg', to='channel.channel'),
        ),
    ]