from django.shortcuts import render,redirect, get_object_or_404
from testapp.forms import UserSignupForm, userDetailsForm
from django.contrib import messages
from testapp.models import UserDetails, UserSignupModel
from django.utils import timezone

def home_view(request):
    return render(request, "home.html")

def UserSignup_view(request):
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User registered successfully")
            return redirect('/login/')
        else:
            messages.error(request, "Enter the details correctly")
    else:
        form = UserSignupForm()
    return render(request, "signup.html", {"form": form})

def UserLogin_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # Check against your signup model for valid credentials
        user_exists = UserSignupModel.objects.filter(username=username, password=password).exists()
        if user_exists:
            request.session["username"] = username
            request.session["login_time"] = timezone.now().timestamp()
            request.session.set_expiry(3600) # 1 hour expiry
            return redirect("/users/")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "signin.html")

def logout_view(request):
    request.session.flush()
    return redirect("/")

def session_protected(view_func):
    # Decorator for session-protected pages
    def wrapper(request, *args, **kwargs):
        username = request.session.get("username")
        login_time = request.session.get("login_time")
        if not username or not login_time:
            return redirect("/")
        # Auto-logout logic (in case browser keeps session)
        if timezone.now().timestamp() - login_time > 3600:
            request.session.flush()
            return redirect("/")
        return view_func(request, *args, **kwargs)
    return wrapper

@session_protected
def userDetails_view(request):
    user_details = UserDetails.objects.all()
    return render(request, "users.html", {"users": user_details})

@session_protected
def usersInsert_view(request):
    if request.method == "POST":
        form = userDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data added successfully")
            return redirect("/users/")
        else:
            messages.error(request, "Please enter valid data")
    else:
        form = userDetailsForm()
    return render(request, "insert.html", {"form": form})

@session_protected
def usersUpdate_view(request, id):
    user_obj = get_object_or_404(UserDetails, pk=id)
    if request.method == "POST":
        form = userDetailsForm(request.POST, instance=user_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Data updated successfully")
            return redirect("/users/")
        else:
            messages.error(request, "Entered details are invalid")
    else:
        form = userDetailsForm(instance=user_obj)
    return render(request, "update.html", {"form": form, "user": user_obj})

@session_protected
def usersDelete_view(request, id):
    user_obj = get_object_or_404(UserDetails, pk=id)
    user_obj.delete()
    messages.success(request, "User deleted successfully")
    return redirect("/users/")
