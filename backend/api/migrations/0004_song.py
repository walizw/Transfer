# Generated by Django 4.1.1 on 2022-09-10 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_user_following'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('album_id', models.DecimalField(decimal_places=0, max_digits=10)),
                ('artist_id', models.DecimalField(decimal_places=0, max_digits=10)),
                ('audio_file', models.FileField(blank=True, default='', upload_to='')),
                ('genre', models.CharField(blank=True, max_length=64, null=True)),
                ('lyrics', models.TextField(blank=True, null=True)),
                ('track_number', models.DecimalField(decimal_places=0, default=0, max_digits=4)),
                ('year', models.DecimalField(decimal_places=0, default=0, max_digits=4)),
            ],
        ),
    ]
