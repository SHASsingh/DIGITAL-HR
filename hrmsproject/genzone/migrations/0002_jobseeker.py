# Generated by Django 3.1.1 on 2020-09-23 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genzone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobSeeker',
            fields=[
                ('applicantname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('contactno', models.CharField(max_length=15)),
                ('emailaddress', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('qualification', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=10)),
                ('keyskills', models.TextField()),
                ('dob', models.CharField(max_length=30)),
                ('regdate', models.CharField(max_length=30)),
            ],
        ),
    ]
