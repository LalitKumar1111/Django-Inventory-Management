from django.urls import path
from .views import *

urlpatterns = [
    path('create-supplier/', create_supplier, name='create-supplier'),
    path('edit-supplier/<int:id>/', edit_supplier,name='edit-supplier'),
    path('delete-supplier/<int:id>/', delete_supplier, name='delete-supplier'),
    path('supplier-list/', SupplierListView, name='supplier-list'),

    path('create-department/', create_department, name='create-department'),
    path('edit_department/<int:id>/', edit_department,name='edit-department'),
    path('delete-department/<int:id>/', delete_department, name='delete-department'),
    path('department-list/', DepartmentListView, name='department-list'),

    path('create-product/', create_product, name='create-product'),
    path('edit-product/<int:id>/', edit_product,name='edit-product'),
    path('delete-product/<int:id>/', delete_product, name='delete-product'),
    path('product-list/', ProductListView, name='product-list'),

    path('create-category/', create_category, name='create-category'),
    path('edit-category/<int:id>/', edit_category,name='edit-category'),
    path('delete-category/<int:id>/', delete_category, name='delete-category'),
    path('category-list/', CategoryListView, name='category-list'),


    path('edit-unit/<int:id>/', edit_unit,name='edit-unit'),
    path('delete-unit/<int:id>/', delete_unit, name='delete-unit'),


    path('create-po/', create_po, name='create-po'),
    path('edit-po/<int:id>/', edit_po, name='edit-po'),
    path('delete-po/<int:id>/', delete_po, name='delete-po'),
    path('po-list/', PoListView, name='po-list'),

    path('create-so/', create_so, name='create-so'),
    path('edit-so/<int:id>/', edit_so, name='edit-so'),
    path('delete-so/<int:id>/', delete_so, name='delete-so'),
    path('so-list/', SoListView, name='so-list'),

    path('create-user/', create_user, name='create-user'),
    path('edit-user/<int:id>/', edit_user,name='edit-user'),
    path('delete-user/<int:id>/', delete_user, name='delete-user'),
    path('user-list/', UserListView, name='user-list'),
]