"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inventory import views
from django.urls import include

urlpatterns = [
    path('', views.home, name='home'),
    path('receive_products/', views.receive_products, name='receive_products'),
    path('add_rack/', views.add_rack, name='add_rack'),
    path('transfer/<str:pk>', views.transfer, name='transfer'),
    path('product_details/<str:pk>/', views.product_details, name='product_details'),
    path('sold/', views.sold, name='sold'),
    path('customers/', views.customers, name='customers'),
    path('suppliers/', views.suppliers, name='suppliers'),
    path('list_products/', views.list_products, name='list_products'),
    path('export_csv',views.export_csv, name="export-csv"),
    path('selproduct_csv',views.selproduct_csv, name="export-csv"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('sell_products/', views.sell_products, name='sell_products'),
    path('sell_qty/<str:pk>/', views.sell_qty, name='sell_qty'),
    path('issue_product/<str:pk>/', views.issue_product, name='issue_product'),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls'))    #django authorization
]
