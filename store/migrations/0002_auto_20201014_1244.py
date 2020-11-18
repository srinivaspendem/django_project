# Generated by Django 3.0.8 on 2020-10-14 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='customer',
            new_name='full_name',
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='catagory',
            field=models.CharField(choices=[('Gpay', 'Gpay'), ('Phonepe', 'Phonepe'), ('Bank Transfer', 'Bank Transfer')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='phone',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]