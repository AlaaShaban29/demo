# Generated by Django 3.2.15 on 2022-09-27 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adhoc_mobile', '0004_remove_answer_extra_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='is_chain',
            field=models.BooleanField(choices=[(False, 'FALSE'), (True, 'True')], default=False),
        ),
        migrations.AlterField(
            model_name='client',
            name='is_disabled',
            field=models.BooleanField(choices=[(False, 'FALSE'), (True, 'True')], default=False),
        ),
        migrations.AlterField(
            model_name='client',
            name='verified',
            field=models.BooleanField(choices=[(False, 'FALSE'), (True, 'True')], default=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='forceOnlineConnectivity',
            field=models.BooleanField(choices=[(False, 'FALSE'), (True, 'True')], default=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='isDisabled',
            field=models.BooleanField(choices=[(False, 'FALSE'), (True, 'True')], default=False),
        ),
        migrations.AlterField(
            model_name='field',
            name='required',
            field=models.BooleanField(choices=[(False, 'FALSE'), (True, 'True')], default=False),
        ),
        migrations.AlterField(
            model_name='plan',
            name='disabled',
            field=models.BooleanField(choices=[(False, 'FALSE'), (True, 'True')], default=False),
        ),
        migrations.AlterField(
            model_name='plan',
            name='force_sequence',
            field=models.BooleanField(choices=[(False, 'FALSE'), (True, 'True')], default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='active',
            field=models.BooleanField(choices=[(False, 'FALSE'), (True, 'True')], default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='auditable',
            field=models.BooleanField(choices=[(False, 'FALSE'), (True, 'True')], default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='frozen_preSale',
            field=models.BooleanField(choices=[(False, 'FALSE'), (True, 'True')], default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='frozen_sale',
            field=models.BooleanField(choices=[(False, 'FALSE'), (True, 'True')], default=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='is_active',
            field=models.BooleanField(choices=[(False, 'FALSE'), (True, 'True')], default=False),
        ),
        migrations.AlterField(
            model_name='route',
            name='disabled',
            field=models.BooleanField(choices=[(False, 'FALSE'), (True, 'True')], default=False),
        ),
        migrations.AlterField(
            model_name='route',
            name='force_sequence',
            field=models.BooleanField(choices=[(False, 'FALSE'), (True, 'True')], default=False),
        ),
        migrations.AlterField(
            model_name='rule',
            name='disabled',
            field=models.BooleanField(choices=[(False, 'FALSE'), (True, 'True')], default=False),
        ),
        migrations.AlterField(
            model_name='rule',
            name='force_sequence',
            field=models.BooleanField(choices=[(False, 'FALSE'), (True, 'True')], default=False),
        ),
        migrations.AlterField(
            model_name='visit',
            name='auto_closed_by_geofence',
            field=models.BooleanField(choices=[(False, 'FALSE'), (True, 'True')], default=False),
        ),
        migrations.AlterField(
            model_name='visit',
            name='end_in_geofence',
            field=models.BooleanField(choices=[(False, 'FALSE'), (True, 'True')], default=False),
        ),
        migrations.AlterField(
            model_name='visit',
            name='start_in_geofence',
            field=models.BooleanField(choices=[(False, 'FALSE'), (True, 'True')], default=False),
        ),
    ]
