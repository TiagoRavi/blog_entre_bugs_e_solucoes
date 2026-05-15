from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os


class Command(BaseCommand):
    help = "Cria um superusuário automaticamente a partir de variáveis de ambiente"

    def handle(self, *args, **options):
        User = get_user_model()

        username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

        if not username or not password:
            self.stdout.write(
                self.style.WARNING("Variáveis de superusuário não configuradas. Pulando criação.")
            )
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.SUCCESS("Superusuário já existe. Nenhuma ação necessária.")
            )
            return

        User.objects.create_superuser(
            username=username,
            email=email or "",
            password=password,
        )

        self.stdout.write(
            self.style.SUCCESS("Superusuário criado com sucesso.")
        )
