from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe


from flightly.users.models import FlightlyUser


@admin.register(FlightlyUser)
class FlightlyUserAdmin(UserAdmin):
    fieldsets = (
        (_('Auth info'), {'fields': ('email', 'password')}),
        (_('Personal info'), {
         'fields': ('first_name', 'last_name', 'photograph_tag', 'photograph')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    ordering = ('first_name',)
    search_fields = ('first_name', 'last_name', 'email')
    readonly_fields = ['photograph_tag']

    def photograph_tag(self, obj):
        return mark_safe(
            f'<img src="{obj.photograph.url}" width="{200}" height={200} />'
        )
