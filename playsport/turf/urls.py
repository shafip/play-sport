from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('bokking/', views.booking,name="booking"),
    path('form/', views.formview, name="form"),
    path('checkout/',views.checkout,name='check'),


]