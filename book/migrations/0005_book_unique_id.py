# Generated by Django 5.0 on 2024-01-02 15:55

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_bannerchild_remove_book_sub_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='unique_id',
            field=models.CharField(blank=True, default=uuid.uuid4, editable=False, max_length=100, null=True, unique=True),
        ),
    ]
