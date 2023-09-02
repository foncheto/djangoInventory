from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
@login_required
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    orders_count = Order.objects.all().count()
    workers_count = User.objects.all().count()
    items_count = Product.objects.all().count()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect("dashboard-index")
    else:
        form = OrderForm()
    context = {
        "orders": orders,
        "form": form,
        "products": products,
        "workers_count": workers_count,
        "orders_count": orders_count,
        "items_count": items_count,
    }
    return render(request, "dashboard/index.html", context)


@login_required
def staff(request):
    workers = User.objects.all()
    workers_count = workers.count()
    orders_count = Order.objects.all().count()
    items_count = Product.objects.all().count
    context = {
        "workers": workers,
        "workers_count": workers_count,
        "orders_count": orders_count,
        "items_count": items_count,
    }
    return render(request, "dashboard/staff.html", context)


@login_required
def staff_detail(request, id):
    worker = User.objects.get(id=id)
    context = {"worker": worker}
    return render(request, "dashboard/staff_detail.html", context)


@login_required
def product(request):
    items = Product.objects.all()
    items_count = items.count()
    orders_count = Order.objects.all().count()
    workers_count = User.objects.all().count()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get("name")
            messages.success(request, f"{product_name} has been added to the inventory")
            return redirect("dashboard-product")
    else:
        form = ProductForm()

    context = {
        "items": items,
        "form": form,
        "items_count": items_count,
        "workers_count": workers_count,
        "orders_count": orders_count,
    }
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
    orders_count = orders.count()
    workers_count = User.objects.all().count()
    items_count = Product.objects.all().count()
    context = {
        "orders": orders,
        "workers_count": workers_count,
        "orders_count": orders_count,
        "items_count": items_count,
    }
    return render(request, "dashboard/order.html", context)
