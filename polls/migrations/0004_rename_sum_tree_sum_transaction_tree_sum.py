# Generated by Django 4.0.2 on 2022-02-18 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_rename_transactions_transaction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='sum_tree_sum',
            new_name='tree_sum',
        ),
    ]