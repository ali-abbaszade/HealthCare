# Generated by Django 3.2.14 on 2022-07-16 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='image',
            field=models.ImageField(default='department/default.jpg', upload_to='department/'),
        ),
    ]
