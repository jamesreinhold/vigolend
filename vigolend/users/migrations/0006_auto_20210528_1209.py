# Generated by Django 3.1.8 on 2021-05-28 10:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        ('users', '0005_auto_20210528_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='country_of_residence',
            field=models.ForeignKey(blank=True, help_text='The country of residence of the customer. KYC Verification will be applied to this country and customer must provide proof of such residence as relevant in the country of jurisdiction.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='locations.country', verbose_name='Country of Residence'),
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='The unique identifier of the customer.', primary_key=True, serialize=False)),
                ('address_line_1', models.CharField(help_text='Address line 2 of the user', max_length=50, verbose_name='Address line 1')),
                ('address_line_2', models.CharField(blank=True, help_text='Address line 2 of the user', max_length=50, null=True, verbose_name='Address line 2')),
                ('state', models.CharField(help_text='Address line 2 of the user', max_length=50, verbose_name='State or Region')),
                ('city', models.CharField(help_text='The city of the address of the user.', max_length=50, verbose_name='City')),
                ('zip_post_code', models.CharField(help_text='The zip or Postal code of the address of the user.', max_length=20, verbose_name='Zip Code')),
                ('country', models.ForeignKey(help_text='Enter field documentation', on_delete=django.db.models.deletion.PROTECT, to='locations.country', verbose_name='Country')),
                ('user', models.ForeignKey(help_text='The user for whom address belongs to.', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User Profile')),
            ],
            options={
                'verbose_name': 'User Address',
                'verbose_name_plural': 'User Addresses',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='current_address',
            field=models.ForeignKey(blank=True, help_text='The current living address of the customer.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='users.useraddress', verbose_name='Current Address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='permanent_address',
            field=models.ForeignKey(blank=True, help_text='The permanent address of the customer.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='users.useraddress', verbose_name='Permanent Address'),
        ),
    ]
