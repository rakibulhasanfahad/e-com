# Generated by Django 4.1.7 on 2023-04-01 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='prod_pic')),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('stock', models.PositiveIntegerField()),
                ('discount_rate', models.PositiveIntegerField()),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.catagory')),
            ],
        ),
    ]
