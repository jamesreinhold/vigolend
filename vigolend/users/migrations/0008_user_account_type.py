# Generated by Django 3.1.8 on 2021-05-28 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_useraddress_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='account_type',
            field=models.CharField(blank=True, choices=[('borrower', 'Borrower'), ('investor', 'Investor')], default='borrower', help_text='The account type of the user.', max_length=8, null=True, verbose_name='Account Tyoe'),
        ),
    ]
