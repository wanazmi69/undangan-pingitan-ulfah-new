# Generated by Django 4.0.5 on 2022-08-27 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypesan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pesan',
            field=models.TextField(max_length=200),
        ),
    ]