from django.shortcuts import render, redirect
from user.models import Account, Quotes

# Create your views here.



def add_admin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        obj = Account(username = username, password = password, type = "admin")
        obj.save()

    return render(request,'add_admin.html')


def index_admin(request):
    return render(request,'index_admin.html')



def view_quotes(request):
    obj = Quotes.objects.filter(status = "pending")
    return render(request,'view_quotes.html',{'quotes': obj})



def update_quotes(request, idd):
    quotes = Quotes.objects.filter(id = idd).update(status = "approved")
    print(quotes)
    return redirect('admin:view_quotes')
