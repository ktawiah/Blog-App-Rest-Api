# Generated by Django 5.0.6 on 2024-06-03 23:58

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import apps.posts.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        db_index=True,
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="id",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        db_index=True, max_length=255, verbose_name="title"
                    ),
                ),
                ("content", models.TextField(verbose_name="content")),
                (
                    "featured_image",
                    models.ImageField(
                        upload_to="images", verbose_name="featured image"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now=True, verbose_name="created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="updated at"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("draft", "DRAFT"),
                            ("published", "PUBLISHED"),
                            ("archived", "ARCHIVED"),
                        ],
                        default=apps.posts.models.Status["DRAFT"],
                        max_length=11,
                        verbose_name="status",
                    ),
                ),
                ("likes", models.IntegerField(verbose_name="likes")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Post",
                "verbose_name_plural": "Posts",
            },
        ),
    ]