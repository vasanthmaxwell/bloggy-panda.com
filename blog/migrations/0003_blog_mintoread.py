# Generated by Django 3.0.6 on 2020-07-30 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_publishdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='mintoread',
            field=models.IntegerField(default=0),
        ),
    ]
