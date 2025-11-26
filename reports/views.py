from django.shortcuts import render
from clients.models import Client
from tasks.models import Task
from deals.models import Deal
from products.models import Product
from django.db.models import Sum
import datetime

def dashboard(request):
    total_revenue = Client.objects.aggregate(Sum("client_value"))["client_value__sum"] or 0
    total_clients = Client.objects.count()
    total_tasks = Task.objects.count()
    total_deals = Deal.objects.count()
    total_products = Product.objects.count()

    return render(request, "dashboard_mobile.html", {
        "total_revenue": total_revenue,
        "total_clients": total_clients,
        "total_tasks": total_tasks,
        "total_deals": total_deals,
        "total_products": total_products,
    })

def reports(request):
    months = []
    values = []

    for i in range(6):
        month = datetime.date.today().replace(day=1) - datetime.timedelta(days=30*i)
        rev = Client.objects.filter(created_at__month=month.month).aggregate(Sum("client_value"))["client_value__sum"] or 0
        months.append(month.strftime("%b"))
        values.append(float(rev))

    # zip months and values into pairs for template convenience
    months_rev = months[::-1]
    values_rev = values[::-1]
    pairs = list(zip(months_rev, values_rev))

    return render(request, "reports/reports.html", {
        "pairs": pairs,
    })
