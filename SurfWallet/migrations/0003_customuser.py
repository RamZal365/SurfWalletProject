# Generated by Django 4.2.1 on 2023-05-11 10:54

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('SurfWallet', '0002_spot_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('birthday', models.DateField()),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('started_surfing', models.DateField(null=True)),
                ('surfing_level', models.PositiveIntegerField(choices=[(1, 'First time'), (2, 'Beginner'), (3, 'Medium-Beginner'), (4, 'Medium'), (5, 'Medium-Advanced'), (6, 'Advanced'), (7, 'Advanced-Pro'), (8, 'Pro')])),
                ('weight', models.FloatField(null=True)),
                ('height', models.FloatField(null=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
