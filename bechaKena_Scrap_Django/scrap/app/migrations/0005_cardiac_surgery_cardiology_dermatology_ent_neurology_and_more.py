# Generated by Django 4.2 on 2023-05-16 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_hospital'),
    ]

    operations = [
        migrations.CreateModel(
            name='CARDIAC_SURGERY',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('degree', models.CharField(max_length=255)),
                ('specialist', models.CharField(max_length=255)),
                ('image_path', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CARDIOLOGY',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('degree', models.CharField(max_length=255)),
                ('specialist', models.CharField(max_length=255)),
                ('image_path', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DERMATOLOGY',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('degree', models.CharField(max_length=255)),
                ('specialist', models.CharField(max_length=255)),
                ('image_path', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ENT',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('degree', models.CharField(max_length=255)),
                ('specialist', models.CharField(max_length=255)),
                ('image_path', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='NEUROLOGY',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('degree', models.CharField(max_length=255)),
                ('specialist', models.CharField(max_length=255)),
                ('image_path', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ORTHOPEDICS',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('degree', models.CharField(max_length=255)),
                ('specialist', models.CharField(max_length=255)),
                ('image_path', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UROLOGY',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('degree', models.CharField(max_length=255)),
                ('specialist', models.CharField(max_length=255)),
                ('image_path', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.RenameModel(
            old_name='Hospital',
            new_name='ANESTHESIOLOGY',
        ),
    ]
