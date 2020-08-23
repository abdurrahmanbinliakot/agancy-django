from django.shortcuts import render, redirect
from .models import Services, TeamMember, About, Clients, Portfolio

# some import for registration form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Create your views here.
#@login_required(login_url='signin')
def index(request):
    services_data = Services.objects.all()
    team_member_data = TeamMember.objects.all()
    about_data = About.objects.all()
    client_data = Clients.objects.all()
    portfolio_data = Portfolio.objects.all()

    if request.user.is_authenticated:
      session = True
    else:
      session = False

    all_index_data = {
        'services_data': services_data,
        'team_members_data': team_member_data,
        'about_data': about_data,
        'clients_data': client_data,
        'portfolios_data': portfolio_data,
        'session':session,
    }


    return render(request, 'index.html', all_index_data)


# Create your views here for login.


def signin(request):
  if request.user.is_authenticated:
        return redirect('index' )
  else:
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'User Name Or password is not Valid!')
    return render(request, 'login.html', {})


# Create your views here for logout.


def UserLogout(request):
    logout(request)
    return redirect('index')
    return render(request, 'login.html', {})

    # Create your views here for registration.


def registration(request):
    if request.user.is_authenticated:
        return redirect('index' )
    else:

        class UserRegistrationForm(
                UserCreationForm
        ):  # We can register with defult form "UserCreationForm"
            class Meta:
                model = User
                fields = ['username', 'email', 'password1', 'password2']

        form = UserRegistrationForm(request.POST)
        if form.is_valid():  #chack form with is_valid() methode
            form.save()  # Save form with save() methode
            user = form.cleaned_data.get('username')
            messages.success(request, 'User has created for ' + user)
            return redirect('signin')

        return render(request, 'registration.html', {'django_form': form})
