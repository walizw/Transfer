from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import _UserChangeForm, _UserCreationForm

class UserAdmin (UserAdmin):
    add_form = _UserCreationForm
    form = _UserChangeForm
    model = User
    list_display = ("name", "email", "is_staff")
    list_filter = ("name", "email", "is_staff")
    fieldsets = (
        (None, {"fields": ("name", "email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "is_admin")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("name", "email", "password", "is_staff")
        })
    )

    search_fields = ("name",)
    ordering = ("name",)

admin.site.register (User, UserAdmin)
