# Generated by Django 5.1 on 2024-10-27 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScannedImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.BinaryField()),
                ('category', models.CharField(choices=[('Plastic', 'Plastic'), ('Metal', 'Metal'), ('Glass', 'Glass')], max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('scan_date', models.DateField()),
                ('isArchived', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'scanned_image',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UnrecognizedImages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[('Plastic', 'Plastic'), ('Metal', 'Metal'), ('Glass', 'Glass')], max_length=50)),
                ('image', models.BinaryField()),
                ('date_registered', models.DateField()),
                ('isArchived', models.BooleanField(default=False)),
                ('isRecognized', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'unrecognized_images',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('profile_picture', models.BinaryField()),
                ('picture_format', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email_address', models.EmailField(max_length=100, primary_key=True, serialize=False)),
                ('college_department', models.CharField(max_length=50)),
                ('user_password', models.CharField(max_length=100)),
                ('isVerified', models.BooleanField(default=False)),
                ('isFirstTime', models.BooleanField(default=True)),
                ('isSuspended', models.BooleanField(default=False)),
                ('isArchived', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phone_number',
        ),
    ]
