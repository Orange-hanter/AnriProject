# Generated by Django 4.2.5 on 2023-12-04 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("products", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="created")),
                ("updated", models.DateTimeField(auto_now=True, verbose_name="updated")),
                ("amount", models.DecimalField(decimal_places=2, max_digits=100)),
                ("address", models.CharField(max_length=256)),
                ("paid", models.BooleanField(default=False)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("FORMATION", "Formation"),
                            ("PAYMENT WAITING", "Payment waiting"),
                            ("DISPATCH WAITING", "Dispatch waiting"),
                            ("SENT", "Sent"),
                            ("SHIPPED", "Shipped"),
                            ("EMERGENCY", "Emergency"),
                        ],
                        default="FORMATION",
                        max_length=64,
                    ),
                ),
                (
                    "payment_method",
                    models.CharField(
                        choices=[("ONLINE", "Online"), ("ON_RECEIPT", "On receipt")], default="ONLINE", max_length=64
                    ),
                ),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="created")),
                ("updated", models.DateTimeField(auto_now=True, verbose_name="updated")),
                ("quantity", models.PositiveIntegerField()),
                ("price", models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True)),
                ("order", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="orders.order")),
                ("product", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="products.product")),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
