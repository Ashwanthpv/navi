from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import csv
from .models import Client
from .forms import ClientForm

def download_clients(request):
    clients = Client.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="clients.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['ID', 'Name', 'Email', 'Phone', 'Company', 'Value'])
    for client in clients:
        writer.writerow([client.id, client.full_name, client.email, client.phone, client.company or '', client.client_value or 0])
    
    return response

def clients_list(request):
    clients = Client.objects.all()
    return render(request, "clients/clients_list_mobile.html", {"clients": clients})

def add_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/clients/")
    else:
        form = ClientForm()
    return render(request, "clients/add_client_mobile.html", {"form": form})

def edit_client(request, id):
    client = get_object_or_404(Client, id=id)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect("/clients/")
    else:
        form = ClientForm(instance=client)
    return render(request, "clients/add_client_mobile.html", {"form": form})

def delete_client(request, id):
    client = get_object_or_404(Client, id=id)
    if request.method == "POST":
        client.delete()
        return redirect("/clients/")
    return render(request, "clients/delete_client.html", {"client": client})
