# Generated by Django 3.1 on 2024-09-20 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20240920_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='default/default-user.png', upload_to='userprofile'),
        ),
    ]
