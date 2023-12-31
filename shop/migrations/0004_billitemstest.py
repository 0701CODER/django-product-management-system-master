# Generated by Django 3.1 on 2020-08-11 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20200811_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillItemsTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productBatch', models.CharField(max_length=50, null=True)),
                ('productPacking', models.CharField(max_length=50, null=True)),
                ('productQuantity', models.IntegerField(default=1)),
                ('productPrice', models.FloatField(default=0)),
                ('productTotalPrice', models.FloatField(default=0)),
                ('productName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bills2', to='shop.productdetailbatch')),
                ('purchaseno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bills2', to='shop.bill')),
            ],
        ),
    ]
