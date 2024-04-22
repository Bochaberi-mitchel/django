from.import views
from django.urls import path
urlpatterns = [
  path('home/', views.home, name='home'),
  path('contact/', views.contact, name='contact'),
  path('about/', views.about, name='about'),
  path('services/', views.services, name='services'),
  path('', views.projectpage, name='projectpage'),






]