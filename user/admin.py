from django.contrib import admin

from .models import User


# Register your models here.
class User(admin.ModelAdmin):
    list_display = (
        'name', 'sex', 'password', 'password', 'qq_name', 'wc_name', 'phone', 'email', 'profession', 'status',
        'created_time')
    list_filter = ('sex', 'status', 'created_time')
    fieldsets = (
        (None, {
            'fields': (
                'name',
                (' sex', ' profession '),
                ('email ', ' qq ', ' phone '),
                'status ',
            )
        })
    )
