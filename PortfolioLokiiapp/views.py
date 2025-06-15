from django.shortcuts import render, redirect
from .forms import PersonForm, SkillForm, ProjectForm, BlogForm, ClientServiceForm
from django.contrib import messages
from .models import Person, Skill, Project, Blog, ClientService
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .decorators import hardcoded_admin_only



# Home Page
def index(request):
    person = Person.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    blogs = Blog.objects.all()
    services = ClientService.objects.all()

    context = {
        'person': person,
        'skills': skills,
        'projects': projects,
        'blogs': blogs,
        'services': services,
    }

    return render(request, 'index.html', context)

# Dashboard View (accessible by hardcoded admin or superuser)
@hardcoded_admin_only
def dashboard(request):
    users = User.objects.all()
    return render(request, 'dashboard.html', {'users': users})


# Add Person Info
@hardcoded_admin_only
def add_person_info(request):
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Person information added successfully!")
            return redirect('addinfoperson')
        else:
            messages.error(request, "Error in form submission.")
    else:
        form = PersonForm()
    return render(request, 'add_person_info.html', {'form': form})


# Add Skill
@hardcoded_admin_only
def add_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'add_skill.html', {'form': form, 'success': 'Skill added successfully!'})
        else:
            return render(request, 'add_skill.html', {'form': form, 'error': 'Error in form.'})
    else:
        form = SkillForm()
    return render(request, 'add_skill.html', {'form': form})


# Add Project
@hardcoded_admin_only
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'add_project.html', {'form': form, 'success': 'Project added successfully!'})
        else:
            return render(request, 'add_project.html', {'form': form, 'error': 'Error in form.'})
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'form': form})


# Add Blog
@hardcoded_admin_only
def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog submitted successfully!')
            return redirect('add_blog')
        else:
            messages.error(request, 'Error in blog form.')
    else:
        form = BlogForm()
    return render(request, 'add_blog.html', {'form': form})


# Add Service
@hardcoded_admin_only
def add_service(request):
    if request.method == 'POST':
        form = ClientServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Service submitted successfully!")
            return redirect('add_service')
        else:
            messages.error(request, "Error submitting service.")
    else:
        form = ClientServiceForm()

    client_services = ClientService.objects.all()
    return render(request, 'add_service.html', {'form': form, 'clientServices': client_services})


# Login View (supports hardcoded and Django admin)
def login_view(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Hardcoded Admin Check
            if username == '#####' and password == '###':
                request.session['is_admin_authenticated'] = True
                return redirect('dashboard')

            # Authenticate from database
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard') if user.is_superuser else redirect('index')
            else:
                form.add_error(None, 'Invalid username or password')

    return render(request, 'login.html', {'form': form})


# Logout View
def logout_view(request):
    request.session.flush()  # Clear hardcoded admin session
    logout(request)  # Django logout
    return redirect('login')

  
# Signup View
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Admin Views
def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user and user.is_staff:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'admin_login.html', {'error': 'Invalid credentials or not an admin'})

    return render(request, 'admin_login.html')

@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('admin_login')

    users = User.objects.all()
    return render(request, 'dashboard.html', {'users': users})

def admin_logout(request):
    logout(request)
    return redirect('admin_login')
