from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader
from .models import Member
from .models import TennisCourt, Reservation
from .forms import ReservationForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Create a User
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            
            # Create a corresponding Member
            member = Member(
                user=user,
                firstname=form.cleaned_data['firstname'],
                lastname=form.cleaned_data['lastname'],
                phone=form.cleaned_data['phone'],
                joined_date=form.cleaned_data['joined_date'],
                age=form.cleaned_data['age'],
            )
            member.save()

            # Log the user in
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)

            return redirect('home')  # Redirect to your home page
    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})
def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  
  return HttpResponse(template.render(context, request))
def court_list(request):
    courts = TennisCourt.objects.all()
    return render(request, 'court_list.html', {'courts': courts})

def court_detail(request, court_id):
    court = TennisCourt.objects.get(id=court_id)
    return render(request, 'court_detail.html', {'court': court})
  
def home(request):
    tennis_courts = TennisCourt.objects.all()
    return render(request, 'home.html', {'tennis_courts': tennis_courts})
  
def login_view(request):
    # Your login logic here
    return render(request, 'login.html')
  
def reservation(request, court_id):
    tennis_court = TennisCourt.objects.get(pk=court_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.court = tennis_court
            reservation.save()
            return redirect('reservation_status')
    else:
        form = ReservationForm()

    return render(request, 'reservation.html', {'form': form, 'tennis_court': tennis_court})

@login_required
def reservation_status(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservation_status.html', {'reservations': reservations})

