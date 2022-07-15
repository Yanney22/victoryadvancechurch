from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum
from django.db.models.functions import ExtractMonth
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse

import calendar
# Create your views here.

# User Dashboard

from home.models import *


def my_dashboard(request):
    if request.user.is_authenticated:
        pay = payments.objects.all()
        payment = pay.annotate(month=ExtractMonth('date_paid')).values('month').annotate(
            count=Count('id')).values('month', 'count').annotate(total_amount=Sum('amount_paid'))
        monthNumber = []
        totalpayments = []

        for d in payment:
            monthNumber.append(calendar.month_name[d['month']])

            totalpayments.append(d['total_amount'])
        ii = 0
        for i in pay:
            ii = ii + i.amount_paid

        return render(request, 'user/dashboard.html', {'monthNumber': monthNumber,
                                                       'totalpayments': totalpayments,
                                                       'all': ii

                                                       }
                      )
    else:

        return HttpResponseRedirect(reverse('admin:index'))


@login_required
def my_purchases(request):
    pay = purchase.objects.all()
    payment = pay.annotate(month=ExtractMonth('date_paid')).values('month').annotate(
        count=Count('id')).values('month', 'count').annotate(total_amount=Sum('amount_paid'))
    monthNumber = []
    totalpayments = []

    for d in payment:
        monthNumber.append(calendar.month_name[d['month']])

        totalpayments.append(d['total_amount'])

    return render(request, 'user/puchases.html', {
        'monthNumber': monthNumber,
        'totalpayments': totalpayments,

    }
                  )
