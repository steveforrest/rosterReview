# Generated by Django 3.2 on 2022-02-07 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0005_comment_commenter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rosterlist',
            old_name='numberOfComments',
            new_name='Comments',
        ),
        migrations.RenameField(
            model_name='rosterlist',
            old_name='numberOfDislikes',
            new_name='Dislikes',
        ),
        migrations.RenameField(
            model_name='rosterlist',
            old_name='numberOfLikes',
            new_name='Likes',
        ),
    ]