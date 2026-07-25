from django.apps import AppConfig
from django.conf import settings
import cloudinary


class BlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"

    def ready(self):
        cloudinary.config(
            cloud_name=settings.CLOUDINARY_STORAGE["CLOUD_NAME"],
            api_key=settings.CLOUDINARY_STORAGE["API_KEY"],
            api_secret=settings.CLOUDINARY_STORAGE["API_SECRET"],
            secure=True,
        )

    def ready(self):
        import blog.signals  # noqa