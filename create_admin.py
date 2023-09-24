import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_portfolio.settings")
django.setup()

from django.contrib.auth.models import User

User.objects.create_superuser('manuel04', 'correo@ejemplo.com', '2005')
