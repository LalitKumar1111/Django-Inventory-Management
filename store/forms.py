from django import forms
from .models import *

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields=['name','email','mobile','address']
        widgets={
            'name':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'email': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'mobile': forms.NumberInput(attrs={
                'class':'form-control'
            }),
            'address': forms.TextInput(attrs={
                'class':'form-control'
            })
        }

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Dept
        fields=['deptname','email','mobile','address']
        widgets={
            'name':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'email': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'mobile': forms.NumberInput(attrs={
                'class':'form-control'
            }),
            'address': forms.TextInput(attrs={
                'class':'form-control'
            })
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields=['name','pcode','category','unit','pricepu','stockinhand','minstacktomaintain']
        widgets={
            'name':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'pcode': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'category': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'unit': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'pricepu': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'stockinhand': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'minstacktomaintain': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields=['catname','catdetails']
        widgets={
            'catname':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'catdetails': forms.TextInput(attrs={
                'class':'form-control'
            }),
        }

class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields=['uname']
        widgets={
            'uname':forms.TextInput(attrs={
                'class':'form-control'
            }),
        }

class POForm(forms.ModelForm):
    class Meta:
        model = PO
        fields=['ponum','podate','supplier','pname','rquantity','uname','priceperunit','amount','deliverystatus','paymentstatus']
        widgets={
            'ponum':forms.TextInput(attrs={
                'class':'form-control'
            }),

            'podate':forms.DateInput(attrs={
                'class':'form-control'
            }),

            'supplier':forms.TextInput(attrs={
                'class':'form-control'
            }),

            'pname': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'rquantity': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'uname': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'priceperunit': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'deliverystatus': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'paymentstatus': forms.TextInput(attrs={
                'class': 'form-control'
            }),

        }
