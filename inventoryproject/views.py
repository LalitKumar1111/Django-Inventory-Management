from django.shortcuts import render



def dashboard(request):
    #p=Product.object.all()
    return render(request, 'dashboard.html')