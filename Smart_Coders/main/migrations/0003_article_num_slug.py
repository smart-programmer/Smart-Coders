# Generated by Django 2.0 on 2018-04-14 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='num_slug',
            field=models.SmallIntegerField(default=1),
        ),
    ]