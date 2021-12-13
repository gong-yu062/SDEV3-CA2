from django.contrib import admin
from .models import Voucher

class VoucherAdmin(admin.ModelAdmin):
    list_display = ['code', 'valid_form', 'valid_to',
                'discount', 'active']
    list_filter = ['active', 'valid_form',]
    search_fields = ['code']

admin.site.register(Voucher,VoucherAdmin)
