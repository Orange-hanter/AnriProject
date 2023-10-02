from django.contrib import admin
from anri.apps.users.models import Employee, Contragent


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("user", "contragent")
    list_filter = ("user",)


@admin.register(Contragent)
class ContragentAdmin(admin.ModelAdmin):
    list_display = (
        "company_name",
        "state_cadastr_address",
        "legal_address",
        "company_rating",
        "contact_name",
        "contact_email",
        "contact_phone",
    )
    list_filter = ("company_name",)
