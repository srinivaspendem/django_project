# Generated by Django 3.0.8 on 2020-10-14 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20201014_1244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='catagory',
            new_name='payment_method',
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='full_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
