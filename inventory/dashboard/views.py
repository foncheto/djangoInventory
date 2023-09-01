from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm
from django.shortcuts import redirect
from django.contrib.auth.models import User


# Create your views here.
@login_required
def index(request):
    return render(request, "dashboard/index.html")


@login_required
def staff(request):
    workers = User.objects.all()
    context = {"workers": workers}
    return render(request, "dashboard/staff.html", context)


@login_required
def staff_detail(request, id):
    worker = User.objects.get(id=id)
    context = {"worker": worker}
    return render(request, "dashboard/staff_detail.html", context)


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


@login_required
def product_delete(request, id):
    item = Product.objects.get(id=id)
    if request.method == "POST":
        item.delete()
        return redirect("dashboard-product")
    return render(request, "dashboard/product_delete.html", context={"item": item})


@login_required
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
    orders = Order.objects.all()
    context = {"orders": orders}
    return render(request, "dashboard/order.html", context)
