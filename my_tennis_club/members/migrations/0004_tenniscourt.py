# Generated by Django 4.2.8 on 2023-12-10 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_member_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='TennisCourt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('court_type', models.CharField(choices=[('grass', 'Grass'), ('hard', 'Hard'), ('clay', 'Clay'), ('carpet', 'Carpet')], max_length=10)),
                ('city', models.CharField(max_length=255)),
            ],
        ),
    ]
