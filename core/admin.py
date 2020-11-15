from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import ExtendedUserCreationForm, ExtendedUserChangeForm
from .models import ExtendedUser


class ExtendedUserAdmin(UserAdmin):
    add_form = ExtendedUserCreationForm
    form = ExtendedUserChangeForm
    model = ExtendedUser
    list_display = ['username',
                    'email',
                    'classification',
                    ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('classification',)}),
    )


admin.site.register(ExtendedUser, ExtendedUserAdmin)
