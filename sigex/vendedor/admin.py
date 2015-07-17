"""
Customizations for the Django administration interface.
"""

from django.contrib import admin
from vendedor.models import Vendedor


admin.site.register(Vendedor)

