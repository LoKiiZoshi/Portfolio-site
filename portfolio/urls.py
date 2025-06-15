"""
URL configuration for Portfolioll project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static
from PortfolioLokiiapp.views import* 
  

urlpatterns = [ 
    path('admin/', admin.site.urls),
    
  path('', index, name='index'),

    path('addinfoperson/', add_person_info, name='addinfoperson'),
    path('addskill/', add_skill, name='addskill'),
    path('add_project/', add_project, name='add_project'),
    path('add_service/', add_service, name='add_service'),
    path('add_blog/', add_blog, name='add_blog'),
    path('dashboard/', dashboard, name='dashboard'),  
 
    path('signup/', signup_view, name='signup'),
  
    path('admin-login/', admin_login, name='admin_login'),
    path('admin-logout/', admin_logout, name='admin_logout'),
    
    path('login/', login_view, name='login'), 
    path('logout/', logout_view, name='logout'),
 

    
]     












# Serving static and media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  