# Generated by Django 4.2 on 2023-10-25 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_more', models.CharField(default='View All', max_length=10)),
                ('currency_sign', models.CharField(default='$', max_length=10)),
                ('currency_abbreviation', models.CharField(default='USD', max_length=10)),
                ('service_fee_percentage', models.IntegerField(default=5, help_text='NOTE: Numbers added here are in percentage (%)ve.g 4%')),
                ('service_fee_flat_rate', models.DecimalField(decimal_places=2, default=0.7, help_text='NOTE: Add the amount you want to charge as service fee e.g $2.30', max_digits=12)),
                ('service_fee_charge_type', models.CharField(choices=[('percentage', 'Percentage'), ('flat_rate', 'Flat Rate')], default='percentage', max_length=30)),
                ('enforce_2fa', models.BooleanField(default=True)),
                ('activate_affiliate_system', models.BooleanField(default=True)),
                ('send_email_notifications', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Settings',
                'verbose_name_plural': 'Settings',
            },
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=500)),
                ('rate', models.IntegerField(default=5, help_text='Numbers added here are in percentage (5 = 5%)')),
                ('active', models.BooleanField(default=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Tax',
            },
        ),
    ]
