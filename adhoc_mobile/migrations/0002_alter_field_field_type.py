# Generated by Django 3.2.15 on 2022-09-26 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adhoc_mobile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='field_type',
            field=models.CharField(choices=[('text', 'text'), ('button', 'button'), ('color', 'color'), ('number', 'number'), ('password', 'password'), ('radio', 'radio'), ('date', 'date'), ('search', 'search'), ('datetime-local', 'datetime-local'), ('email', 'email'), ('file', 'file'), ('hidden', 'hidden'), ('image', 'image'), ('month', 'month')], default='text', max_length=20),
        ),
    ]
