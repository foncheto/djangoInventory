from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.index, name="dashboard-index"),
    path("staff/", views.staff, name="dashboard-staff"),
    path("staff/detail/<int:id>/", views.staff_detail, name="dashboard-staff-detail"),
    path("product/", views.product, name="dashboard-product"),
    path(
        "product/delete/<int:id>/",
        views.product_delete,
        name="dashboard-product-delete",
    ),
    path(
        "product/update/<int:id>/",
        views.product_update,
        name="dashboard-product-update",
    ),
    path("order/", views.order, name="dashboard-order"),
]
