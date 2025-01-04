from django.urls import path
from . import views
from django.urls import path
from .views import SignupAPIView

urlpatterns = [
    path('', views.home, name='home'),  # Home page route
    path('login/', views.login_view, name='login'),  # Login route
    path('signup/', views.signup_view, name='signup'),  # Signup route
    path('signup/', SignupAPIView.as_view(), name='signup'),
    # path('logout/', views.logout_user, name='logout'),  # Logout route
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard route
    path('list-rooms/', views.list_rooms, name='list_rooms'),  # List rooms route
    path('list-customers/', views.list_customers, name='list_customers'),  # List customers route
    path('add-room/', views.add_room, name='add_room'),  # Add room route
    path('add-customer/', views.add_customer, name='add_customer'),  # Add customer route
    path('update-room/<int:room_id>/', views.update_room, name='update_room'),  # Update room route
    path('update-customer/<int:customer_id>/', views.update_customer, name='update_customer'),  # Update customer route
    path('delete-room/<int:room_id>/', views.delete_room, name='delete_room'),  # Delete room route
    path('delete-customer/<int:customer_id>/', views.delete_customer, name='delete_customer'),  # Delete customer route
    path("faq/", views.faq_view, name="faq"),
    path('contact-us/', views.contact_us, name='contact_us'),
]
