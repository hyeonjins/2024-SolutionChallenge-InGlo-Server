# Generated by Django 4.2.6 on 2024-02-20 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0007_issue_article_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='article_id',
        ),
    ]
