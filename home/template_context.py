from .models import *
from django.db.models import Min, Max


def get_filters(request):
    our1 = our.objects.all();
    pay = payments.objects.distinct().values('payment_types__name', 'payment_types__id')
    ourpurchase = purchase.objects.distinct().values('purchase_types__purchase_type', 'purchase_types__id')
    partone = [],
    parttwo = []
    for i in our1:
        partone = i.name[0:8]
        parttwo = i.name[8:27]
    data = {
        'pay': pay,
        'ourpurchase': ourpurchase,
        'our': our1,
        'partone': partone,
        'parttwo': parttwo,
    }
    return data
