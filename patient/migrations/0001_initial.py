# Generated by Django 5.1.6 on 2025-02-24 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patID', models.BigAutoField(primary_key=True, serialize=False)),
                ('patName', models.CharField(max_length=200)),
                ('patBDate', models.DateField(null=True)),
                ('patAddress', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
