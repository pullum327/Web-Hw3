from django.urls import path
from . import views
from .views import court_list, court_detail
from .views import login_view, home, reservation, reservation_status
urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('court/', court_list, name='court_list'),
    path('court/<int:court_id>/', court_detail, name='court_detail'),
    path('login/', login_view, name='login'),
    path('home/', home, name='home'),
    path('reservation/<int:court_id>/', reservation, name='reservation'),
    path('reservation_status/', reservation_status, name='reservation_status'),
]