# Generated by Django 4.1.5 on 2023-01-03 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_alter_user_bio_alter_user_birth_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('album', models.CharField(max_length=200)),
                ('artist', models.CharField(max_length=100)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('genre', models.CharField(choices=[('HH', 'Hip-Hop/Rap'), ('PO', 'Pop'), ('RO', 'Rock'), ('CO', 'Country'), ('ALT', 'Alternative')], max_length=3)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
