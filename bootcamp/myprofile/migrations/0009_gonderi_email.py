# Generated by Django 4.0.4 on 2022-05-20 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0008_rename_first_name_gonderi_icerik_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gonderi',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
