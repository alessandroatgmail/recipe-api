from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUSerAdmin
from core import models
from django.utils.translation import gettext as _
# Register your models here.


class UserAdmin(BaseUSerAdmin):
    ordering = ["id"]
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
        }),
    )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Tag)
