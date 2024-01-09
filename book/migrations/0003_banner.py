# Generated by Django 5.0 on 2024-01-02 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_audio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='banner/')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tag', models.CharField(blank=True, max_length=100, null=True)),
                ('tur', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
