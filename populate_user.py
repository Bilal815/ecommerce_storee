import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings.development")
django.setup()

from ecommerce.asgi import get_default_application

application = get_default_application()

from hcm.models import Account


# write script
def populate(n):
    for i in range(1, n + 1):
        user = Account()
        user.user_id = i
        user.set_password("password")
        user.is_employee = True
        user.save()
    user = Account()
    user.user_id = 0
    user.set_password("password")
    user.is_employee = False
    user.is_employer = True
    user.save()


# end script
if __name__ == '__main__':
    populate(11)
