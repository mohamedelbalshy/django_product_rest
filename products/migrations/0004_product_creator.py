# Generated by Django 4.1.7 on 2023-02-26 20:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("products", "0003_alter_product_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="creator",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
