"""
WSGI config for ecommerce project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys

# Add the path to the outer "Eshop" directory
outer_eshop_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if outer_eshop_dir not in sys.path:
    sys.path.append(outer_eshop_dir)

# Add the path to the inner "ecommerce" directory
inner_ecommerce_dir = os.path.dirname(os.path.abspath(__file__))
if inner_ecommerce_dir not in sys.path:
    sys.path.append(inner_ecommerce_dir)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.ecommerce.settings')

application = get_wsgi_application()
