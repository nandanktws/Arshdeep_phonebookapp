# Generated by Django 4.1.5 on 2023-01-04 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phoneapp', '0002_alter_phonebook_contactnum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonebook',
            name='contactnum',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
