# Generated by Django 4.0.2 on 2022-03-25 13:56

from django.db import migrations, models
import utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=50)),
                ('other_names', models.CharField(blank=True, max_length=200, null=True)),
                ('ghana_card_number', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('code', models.CharField(default=utils.gen_code, max_length=50, unique=True)),
                ('sex', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], max_length=6)),
                ('date_of_birth', models.DateField()),
                ('height', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
