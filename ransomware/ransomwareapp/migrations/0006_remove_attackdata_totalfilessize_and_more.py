# Generated by Django 4.2.4 on 2023-08-30 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ransomwareapp', '0005_alter_attackdata_encryptionkey'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attackdata',
            name='TotalFilesSize',
        ),
        migrations.AddField(
            model_name='attackdata',
            name='TotalFileSize',
            field=models.IntegerField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attackdata',
            name='NumberOfFiles',
            field=models.IntegerField(max_length=100),
        ),
    ]
