# Generated by Django 4.2.1 on 2023-05-03 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0002_orderdetails'),
    ]

    operations = [
        migrations.AlterModelTableComment(
            name='client',
            table_comment='Client',
        ),
        migrations.AlterModelTableComment(
            name='farmer',
            table_comment='Farmer',
        ),
        migrations.AlterModelTableComment(
            name='order',
            table_comment='Order',
        ),
        migrations.AlterModelTableComment(
            name='orderdetails',
            table_comment='OrderDetails',
        ),
        migrations.AlterModelTableComment(
            name='product',
            table_comment='Product',
        ),
    ]
