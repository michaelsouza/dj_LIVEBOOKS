# Generated by Django 4.1.5 on 2023-01-06 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_bookinstance_options_bookinstance_borrower'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back', 'book'], 'permissions': [('can_mark_returned', 'Set book as returned')]},
        ),
    ]
