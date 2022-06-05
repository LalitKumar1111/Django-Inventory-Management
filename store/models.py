from django.db import models

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=220)
    mobile = models.IntegerField()
    address = models.CharField(max_length=220)

    def __str__(self):
        return self.name

class Dept(models.Model):
    deptname = models.CharField(max_length=120, unique=True)
    email = models.CharField(max_length=220)
    mobile = models.IntegerField()
    address = models.CharField(max_length=220)

    def __str__(self):
        return self.name


class Category(models.Model):
    catname=models.CharField(max_length=120,unique=True)
    catdetails = models.CharField(max_length=220)
    def __str__(self):
        return self.catname

class Unit(models.Model):
    uname=models.CharField(max_length=120,unique=True)

    def __str__(self):
        return self.uname

class Product(models.Model):
    name = models.CharField(max_length=120, unique=True)
    pcode = models.CharField(max_length=120, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, default=1)
    pricepu = models.IntegerField()
    stockinhand = models.IntegerField()
    minstacktomaintain = models.IntegerField()

    def __str__(self):
        return self.name


class PO(models.Model):
    DELIVERY_CHOICE=(
        ('Delivered', 'Delivered'),
        ('Undelivered', 'Undelivered'),)
    PAYMENT_CHOICE=(
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),)

    ponum = models.CharField(max_length=120, unique=True)
    podate= models.DateField(null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, default=1)
    pname = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    rquantity = models.IntegerField()
    uname = models.ForeignKey(Unit, on_delete=models.CASCADE, default=1)
    priceperunit = models.IntegerField()
    amount = models.IntegerField()
    deliverystatus = models.CharField(max_length=30,choices=DELIVERY_CHOICE,null=True)
    paymentstatus = models.CharField(max_length=30,choices=PAYMENT_CHOICE,null=True)

    def __str__(self):
        return self.ponum
