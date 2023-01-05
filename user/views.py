from django.shortcuts import render, redirect
from user.models import User, Account, Quotes

# Create your views here.


def index(request):
    return render(request,'index.html')



def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = Account.objects.get(username = username, password = password)
            request.session['userid'] = user.id
            if (user.type == 'customer'):
                return redirect('user:after_login')
            elif(user.type == 'admin'):
                return redirect('admin:index_admin')
        except:
            return render(request, 'login.html',{'message':'username or password is incorrect'})

    return render(request,'login.html')





def register_user(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        username = request.POST['username']
        password = request.POST['password']


        obj = User( name=name, email=email, contact=contact)
        obj.save()
        account = Account( username = username, password = password, type = 'customer', user_id = obj.id )
        account.save()
    return render(request,'register_user.html')




def after_login(request):
    if request.method == 'POST':
        quotes = request.POST['quotes']

        obje = Quotes(quotes = quotes, user_id = request.session['userid'])
        obje.save()
    ob = Quotes.objects.filter(status = "approved")
    return render(request,'after_login.html',{'quotes':ob})