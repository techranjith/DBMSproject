# Generated by Django 4.0.5 on 2022-06-19 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_seller_alter_product_sellerid'),
    ]

    operations = [
        migrations.CreateModel(
            name='soldproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantitywished', models.IntegerField()),
                ('cid', models.ForeignKey(null=b'I01\n', on_delete=django.db.models.deletion.SET_NULL, to='store.customer')),
                ('pid', models.ForeignKey(null=b'I01\n', on_delete=django.db.models.deletion.SET_NULL, to='store.product')),
            ],
            options={
                'unique_together': {('pid', 'cid')},
            },
        ),
    ]
