# Generated by Django 4.0.2 on 2022-03-25 13:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('visit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TestType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LabTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('lab_technician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labs', to=settings.AUTH_USER_MODEL)),
                ('test_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labs', to='lab.testtype')),
                ('visit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labs', to='visit.visit')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
