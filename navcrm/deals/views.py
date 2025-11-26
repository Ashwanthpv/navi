from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import csv
from .models import Deal
from .forms import DealForm

def download_deals(request):
    deals = Deal.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="deals.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['ID', 'Name', 'Client', 'Value', 'Stage'])
    for deal in deals:
        writer.writerow([deal.id, deal.name, deal.client or '', deal.value or 0, deal.get_stage_display()])
    
    return response

def deals_list(request):
    deals = Deal.objects.all()
    return render(request, 'deals/deals_list_mobile.html', {'deals': deals})

def add_deal(request):
    if request.method == 'POST':
        form = DealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/deals/')
    else:
        form = DealForm()
    return render(request, 'deals/add_deal_mobile.html', {'form': form})

def edit_deal(request, id):
    deal = get_object_or_404(Deal, id=id)
    if request.method == 'POST':
        form = DealForm(request.POST, instance=deal)
        if form.is_valid():
            form.save()
            return redirect('/deals/')
    else:
        form = DealForm(instance=deal)
    return render(request, 'deals/add_deal_mobile.html', {'form': form})

def delete_deal(request, id):
    deal = get_object_or_404(Deal, id=id)
    if request.method == 'POST':
        deal.delete()
        return redirect('/deals/')
    return render(request, 'deals/delete_deal.html', {'deal': deal})
