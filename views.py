from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .models import Room, Customer, Employee
from .forms import RoomForm, CustomerForm, EmployeeForm, SignUpForm  # Import the SignUpForm
from django.contrib.auth import login
from django.shortcuts import redirect
from .serializers import SignupSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SignupAPIView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)  # Automatically log the user in
            return redirect('dashboard')  # Redirect to dashboard after signup
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# FAQ view
def faq_view(request):
    faqs = [
        {"question": "What to do if I forgot my password?",
         "answer": "An email has been sent to you for password retrieval."},
        {"question": "How do I book a room?",
         "answer": "To book a room, simply click 'Add Room' and enter the details."},
        {"question": "How do I check customer details?",
         "answer": "Click 'View Customer' and then click 'Edit' to see the details."},
    ]
    return render(request, 'hotel/faq.html', {'faqs': faqs})

# Contact us views
def contact_us(request):
    return render(request, 'hotel/contact_us.html')
# Home View
def home(request):
    return render(request, 'hotel/home.html')

# Login View
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'hotel/login.html')

# Sign Up View
def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user to the database
            login(request, user)  # Automatically log in the user after signup
            messages.success(request, "Account created successfully.")
            return redirect('dashboard')  # Redirect to the dashboard after successful signup
    else:
        form = SignUpForm()
    return render(request, 'hotel/signup.html', {'form': form})

# Dashboard View
@login_required
def dashboard(request):
    return render(request, 'hotel/dashboard.html')

# List Rooms View
@login_required
def list_rooms(request):
    rooms = Room.objects.all()  # Retrieve all room records
    return render(request, 'hotel/list_rooms.html', {'rooms': rooms})

# List Customers View
@login_required
def list_customers(request):
    customers = Customer.objects.all()  # Retrieve all customer records
    return render(request, 'hotel/list_customers.html', {'customers': customers})

# Add Room View
@login_required
def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Room added successfully!")
            return redirect('dashboard')  # Redirect to the dashboard
    else:
        form = RoomForm()
    return render(request, 'hotel/add_room.html', {'form': form})

# Add Customer View
@login_required
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer added successfully!")
            return redirect('dashboard')  # Redirect to the dashboard
    else:
        form = CustomerForm()
    return render(request, 'hotel/add_customer.html', {'form': form})

# Update Room View
@login_required
def update_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            messages.success(request, "Room updated successfully!")
            return redirect('list_rooms')  # Redirect to the room list
    else:
        form = RoomForm(instance=room)
    return render(request, 'hotel/update_room.html', {'form': form})

# Update Customer View
@login_required
def update_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer updated successfully!")
            return redirect('list_customers')  # Redirect to the customer list
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'hotel/update_customer.html', {'form': form})

# Delete Room View
@login_required
def delete_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        room.delete()
        messages.success(request, "Room deleted successfully!")
        return redirect('list_rooms')  # Redirect to the room list
    return render(request, 'hotel/delete_room.html', {'room': room})

# Delete Customer View
@login_required
def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        customer.delete()
        messages.success(request, "Customer deleted successfully!")
        return redirect('list_customers')  # Redirect to the customer list
    return render(request, 'hotel/delete_customer.html', {'customer': customer})
