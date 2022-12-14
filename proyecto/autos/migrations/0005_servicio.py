# Generated by Django 4.0.6 on 2022-07-31 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0004_autos_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('price', models.FloatField()),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('creation_date', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]
