# Generated by Django 5.1 on 2024-08-28 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0008_alter_customer_membership"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="members",
        ),
        migrations.AlterField(
            model_name="order",
            name="placed_at",
            field=models.DateField(auto_now_add=True),
        ),
    ]
