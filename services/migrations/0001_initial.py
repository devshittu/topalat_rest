# Generated by Django 3.1.6 on 2021-02-14 20:27

import django.contrib.postgres.fields.hstore
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='updated at')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='deleted at')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=80, null=True)),
                ('code_name', models.SlugField(unique=True)),
                ('is_available', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'service_category',
                'verbose_name_plural': 'service_categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='updated at')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='deleted at')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=80, null=True)),
                ('code_name', models.SlugField(unique=True)),
                ('is_available', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'service_provider',
                'verbose_name_plural': 'services_providers',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='TransactionLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='updated at')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='deleted at')),
                ('email', models.EmailField(max_length=254, verbose_name='customer email address')),
                ('reference', models.CharField(db_index=True, max_length=32, unique=True)),
                ('description', models.CharField(blank=True, max_length=80, null=True)),
                ('service_category_raw', models.CharField(blank=True, max_length=80, null=True)),
                ('service_provider_raw', models.CharField(blank=True, max_length=80, null=True)),
                ('service_type', models.CharField(choices=[('AT', 'Airtime'), ('DB', 'Data Bundle'), ('CT', 'Cable TV'), ('EL', 'Power Bills')], default='AT', max_length=5)),
                ('payment_status', models.IntegerField(choices=[(1, 'Unprocessed'), (2, 'Processed'), (3, 'Error')], default=1)),
                ('service_render_status', models.IntegerField(choices=[(1, 'Unprocessed'), (2, 'Processed'), (3, 'Error')], default=1)),
                ('service_request_payload_data', django.contrib.postgres.fields.hstore.HStoreField()),
            ],
            options={
                'verbose_name': 'transaction_log',
                'verbose_name_plural': 'transaction_logs',
            },
        ),
    ]
