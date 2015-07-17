"""
Customizations for the Django administration interface.
"""

from django.contrib import admin
from app.models import Company, UserCompany, Navigation


class UserCompanyInline(admin.TabularInline):
    """Choice objects can be edited inline in the Poll editor."""
    model = UserCompany

class CompanyAdmin(admin.ModelAdmin):
    """Definition of the Poll editor."""
    inlines = [UserCompanyInline]


class NavigationAdmin(admin.ModelAdmin):
    list_filter = ('submenu',)

admin.site.register(Company, CompanyAdmin)
admin.site.register(Navigation,NavigationAdmin)
