# Generated by Django 4.1.4 on 2022-12-28 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dev", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="codeup",
            options={
                "ordering": ["code_up"],
                "verbose_name": "Code Up",
                "verbose_name_plural": "Code Up",
            },
        ),
    ]