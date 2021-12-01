# Generated by Django 3.1.7 on 2021-12-01 03:47

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_auto_20211028_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='skill_set',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Python', 'Python'), ('AWS', 'AWS'), ('Azure', 'Azure')], default='none', max_length=16),
        ),
    ]
