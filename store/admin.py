from django.contrib import admin
from .models import *

# Register your models here.
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','mobile','address']

admin.site.register(Supplier,SupplierAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id','deptname','email','mobile','address']

admin.site.register(Dept,DepartmentAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','pcode','category','unit','pricepu','stockinhand','minstacktomaintain']

admin.site.register(Product,ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','catname','catdetails']

admin.site.register(Category,CategoryAdmin)

class UnitAdmin(admin.ModelAdmin):
    list_display = ['id','uname']

admin.site.register(Unit,UnitAdmin)

class POAdmin(admin.ModelAdmin):
    list_display = ['id','ponum','podate','supplier','pname','rquantity','uname','priceperunit','amount','deliverystatus','paymentstatus']

admin.site.register(PO,POAdmin)

class SOAdmin(admin.ModelAdmin):
    list_display = ['id','sonum','sodate','deptname','username','pname','rquantity','uname','priceperunit','amount','deliverystatus']

admin.site.register(SO,SOAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ['id','deptname','name','email','mobile']

admin.site.register(Users,UserAdmin)