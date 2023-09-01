from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('get_address/', views.get_address, name='get_address'),

    path('create_service_request/', views.create_service_request, name='create_service_request'),
    path('driver_dashboard/', views.driver_dashboard, name='driver_dashboard'),
    path('accept_request/<int:request_id>/', views.accept_request, name='accept_request'),
    path('decline_request/<int:request_id>/', views.decline_request, name='decline_request'),
]
