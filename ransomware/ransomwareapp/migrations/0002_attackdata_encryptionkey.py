# Generated by Django 4.2.4 on 2023-08-30 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ransomwareapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attackdata',
            name='EncryptionKey',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
