from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('shop/', views.shop, name='shop'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('WebApplications/', views.web, name='webApplications'),
    path('GraphicalApplications/', views.desktop, name='DesktopApplications'),
    path('ConsoleApplications/', views.console, name='ConsoleApplications'),
    path('frontend/', views.frontend, name='frontend'),
    path('backend/', views.backend, name='backend'),
    path('search/<keyword>', views.search, name='search'),
    path('subscribe/<email>', views.sub, name='subscribe'),
    path('view/<Product_Name>/<ID_of_the_Product>', views.view, name='view'),
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile_view, name="profile"),
    path("list-product/", views.list_product, name="list_product"),
    path("my-products/", views.my_products, name="my_products"),
    path("delete-product/<int:product_id>/", views.delete_product, name="delete_product"),
]