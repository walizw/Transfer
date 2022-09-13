# Generated by Django 4.1.1 on 2022-09-13 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_id', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=64)),
                ('actor', models.CharField(max_length=255)),
                ('object', models.TextField()),
            ],
        ),
    ]