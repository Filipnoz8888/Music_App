# Generated by Django 2.0.4 on 2018-05-03 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20180504_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='yt_link',
            field=models.CharField(default=None, max_length=1000),
            preserve_default=False,
        ),
    ]