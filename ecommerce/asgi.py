import os
import django
from ecommerce.routing import get_default_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings.staging")
django.setup()
application = get_default_application()
