# Register your models here.
from django.contrib import admin

from home.models import *


class MemberTypeAdmin(admin.ModelAdmin):
    list_display = ('member_type', 'date_added')
    search_fields = ('id', 'member_type')


admin.site.register(membertype, MemberTypeAdmin)


class MemberAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'picture',
        'date_of_birth',
        'mobile_number',
        'residential_address',
        'membertype',
        'date_started',
        'any_relative',
        'relative_phone',
        'date_added'
    )

    search_fields = (
        'id',
        'name',
        'mobile_number',
        'residential_address',
        'any_relative',
        'relative_phone'
    )

    list_filter = (
        'date_of_birth',
        'membertype',
        'date_started',
        'date_added'
    )


admin.site.register(member, MemberAdmin)


class PaymentType(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_added')
    search_fields = ('id', 'name', 'date_added')


admin.site.register(paymenttype, PaymentType)


class PaymentMethod(admin.ModelAdmin):
    list_display = ('id', 'paymentmethod', 'date_added')
    search_fields = ('id', 'paymentmethod', 'date_added')


admin.site.register(paymentmethod, PaymentMethod)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'payment_types',
                    'paid_by',
                    'picture',
                    'reference',
                    'amount_paid',
                    'date_added')

    search_fields = (
        'id',
        'paid_by__name',
        'reference',
        'amount_paid'
    )

    list_filter = (
        'payment_types',
        'date_added'
    )


admin.site.register(payments, PaymentAdmin)


class PurchaseTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'purchase_type', 'date_added')
    search_fields = ('id', 'purchase_type', 'date_added')


admin.site.register(purchase_type, PurchaseTypeAdmin)


class PurchasesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'purchase_types',
        'paid_by',
        'reference',
        'picture',
        'amount_paid',
        'date_paid',
        'date_added')

    search_fields = (
        'purchase_types__purchase_type',
        'paid_by__name',
        'reference',
        'picture',
        'amount_paid',
        'date_paid',
        'date_added')

    list_filter = (
        'purchase_types',
        'date_added'
    )


class DocumentAdmin(admin.ModelAdmin):
        list_display = (
            'name',
        'picture' ,
        'picture2' ,
        'picture3',

        'file',
        'reference' ,

        'date_made',
        'date_added'

        )
        search_fields = ('name',  'reference' )

        list_filter = (
            'date_made',
            'date_added'
        )
admin.site.register(documents,DocumentAdmin)
admin.site.register(purchase, PurchasesAdmin)
admin.site.register(our)
