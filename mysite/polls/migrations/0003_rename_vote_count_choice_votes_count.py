# Generated by Django 4.0.6 on 2022-07-23 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_votes_choice_vote_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='vote_count',
            new_name='votes_count',
        ),
    ]
