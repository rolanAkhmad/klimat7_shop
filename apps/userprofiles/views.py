from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import SignUpForm, LoginForm

from apps.store.models import Product

def login_signup(request):
    try:
        if request.POST['login-username'] and request.POST['login-password']:
            username = request.POST['login-username']
            password = request.POST['login-password']
            if username and password:
                print("lol")
                authenticate(username=username, password=password)
                print(username, password)
                login(request, user=User.objects.get(username=username))
                return redirect('index')
    except:
        print("except")

    if request.method == "POST":
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            login(request, user)
            return redirect('index')
        else:
            print("not_valid")
    else:
        signup_form = SignUpForm()

    boiler_list = Product.objects.filter(category__slug="gas_boiler")

    gas_burners = Product.objects.filter(category__slug="gas_burners")
    binary_burners = Product.objects.filter(category__slug="binary_burners")
    liquid_fuel_burners = Product.objects.filter(category__slug="liquid_fuel_burners")

    burners_list = gas_burners | binary_burners | liquid_fuel_burners

    context = {
        'signup_form': signup_form,
        'boiler_list': boiler_list,
        'burners_list': burners_list
    }

    return render(request, 'login-signup.html', context)



