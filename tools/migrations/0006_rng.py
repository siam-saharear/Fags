# Generated by Django 5.0 on 2024-07-30 16:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tools", "0005_meat_type_remove_product_product_catagory_cuts_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Rng",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("array", models.CharField(max_length=1000)),
            ],
        ),
    ]
