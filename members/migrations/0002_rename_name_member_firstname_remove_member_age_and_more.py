# Generated by Django 4.1.7 on 2023-03-22 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='name',
            new_name='firstname',
        ),
        migrations.RemoveField(
            model_name='member',
            name='age',
        ),
        migrations.RemoveField(
            model_name='member',
            name='date',
        ),
        migrations.RemoveField(
            model_name='member',
            name='email',
        ),
        migrations.AddField(
            model_name='member',
            name='lastname',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
