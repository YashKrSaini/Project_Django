# Generated by Django 3.1.6 on 2021-03-23 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210323_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='image',
            field=models.ImageField(default='', upload_to='home/Images'),
        ),
    ]
