from django.db import migrations


def populate_code(apps, schema_editor):
    Product = apps.get_model("catalog", "Product")
    for product in Product.objects.all():
        product.code = f"PROD-{product.pk:05d}"
        product.save(update_fields=["code"])


def clear_code(apps, schema_editor):
    Product = apps.get_model("catalog", "Product")
    Product.objects.update(code=None)


class Migration(migrations.Migration):

    dependencies = [
    ("catalog", "0004_add_product_code"),
]

    operations = [
        migrations.RunPython(populate_code, clear_code),
    ]