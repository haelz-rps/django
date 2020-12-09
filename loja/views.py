from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required

from .forms import AddressForm
from .models  import Address, STATES_CHOICES


def login(request):
    if request.method == "GET":
        return render(request, "myapp/login.html")
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = authenticate(username=username, password=password)

    if user:
        django_login(request,user)
        return redirect("/home/")
    message = "Credenciais inválidas"
    return render(request, "myapp/login.html", {"message": message})

@login_required(login_url='/login')
def home(request):
    return render(request,"myapp/home.html")

@login_required(login_url='/login')
def logout(request):
    django_logout(request)
    return redirect("/login/")

@login_required(login_url='/login')
def address_list(request):
    addresses = Address.objects.all().filter().order_by()
    return render(request, 'address/list.html', {'addresses': addresses})

@login_required(login_url="/login")
def address_create(request):
    form_submitted = False
    if request.method == "GET":
        form = AddressForm()
    else:
        form_submitted = True
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            #Address.objects.create(
            #    address= form.cleaned_data["address"],
            #    address_complement= form.cleaned_data["address_complement"],
            #    city= form.cleaned_data["city"],
            #    state= form.cleaned_data["state"],
            #    country= form.cleaned_data["country"],
            #    user= request.user
            #)
            return redirect(reverse("loja:address_list"))
    return render(request, "address/create.html", {"form": form,"form_submitted": form_submitted})

@login_required(login_url="/login")
def address_update(request, id):
    form_submitted = False
    address =  Address.objects.get(id=id)
    if request.method == "GET":
        #states = STATES_CHOICES
        #form = AddressForm(address.__dict__)
        form = AddressForm(instance=address)
    else:
        form_submitted = True
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return redirect(reverse("loja:address_list"))
        #     address.address = request.POST.get("address")
        #     address.address_complement = request.POST.get("address_complement")
        #     address.city = request.POST.get("city")
        #     address.state = request.POST.get("state")
        #     address.country = request.POST.get("country")
        #     #address.user = request.user



    return render(request, "address/update.html", {"address": address, "form": form, "form_submitted": form_submitted})

@login_required(login_url="/login")
def address_delete(request, id):
    address =  Address.objects.get(id=id)
    if request.method == "GET":
        form = AddressForm(instance=address)
    else:
        address.delete()
        return redirect(reverse("loja:address_list"))

    return render(request, "address/destroy.html", {"address": address, "form": form})


