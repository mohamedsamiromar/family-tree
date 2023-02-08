from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin



class UserAdmin(BaseUserAdmin):

    fieldsets = (
        (None, {'fields': ('email', 'password', 'username')}),
        (('Personal info'), {
         'fields': ('first_name', 'last_name')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                      'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    list_display = ['username', 'email', 'first_name',
                    'last_name', 'is_staff', 'get_user_groups']
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('email', )

    def get_user_groups(self, obj):
        groups = []
        for group in obj.groups.all():
            groups.append(group.name)

        return ', '.join(groups)
    get_user_groups.short_description = 'Groups'

    # readonly_fields = ['is_email_verified', 'email_verification_token']


# Register your models here.
admin.site.register(User, UserAdmin)
