# Generated by Django 4.0 on 2024-02-02 01:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_productpictures_productpicture_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productpicture',
            old_name='picture',
            new_name='image',
        ),
    ]
