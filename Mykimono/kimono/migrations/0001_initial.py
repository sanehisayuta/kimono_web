# Generated by Django 2.2.5 on 2020-01-01 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('0', 'Not know'), ('1', 'Male'), ('2', 'FeMale'), ('9', 'Not applicable')], max_length=1, verbose_name='gender')),
                ('email', models.EmailField(max_length=50)),
                ('mobile_number', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('pay_type', models.CharField(max_length=10, verbose_name='Pay Type')),
                ('card_number', models.IntegerField()),
                ('expiry_date', models.CharField(max_length=10, verbose_name='Expiry Date')),
                ('expiry_year', models.CharField(max_length=10, verbose_name='year')),
                ('security_code', models.CharField(max_length=5)),
                ('free_zone', models.TextField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
