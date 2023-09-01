from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm
from django.shortcuts import redirect


# Create your views here.
@login_required
def index(request):
    return render(request, "dashboard/index.html")


@login_required
def staff(request):
    return render(request, "dashboard/staff.html")


@login_required
def product(request):
    items = Product.objects.all()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard-product")
    else:
        form = ProductForm()

    context = {"items": items, "form": form}
    return render(request, "dashboard/product.html", context)


def product_delete(request, id):
    item = Product.objects.get(id=id)
    if request.method == "POST":
        item.delete()
        return redirect("dashboard-product")
    return render(request, "dashboard/product_delete.html", context={"item": item})


def product_update(request, id):
    item = Product.objects.get(id=id)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("dashboard-product")
    else:
        form = ProductForm(instance=item)

    context = {"form": form, "item": item}
    return render(request, "dashboard/product_update.html", context)


@login_required
def order(request):
    return render(request, "dashboard/order.html")
