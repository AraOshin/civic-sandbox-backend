# """civic_sandbox URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/2.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]



from rest_framework_swagger.views import get_swagger_view

"""Civic Sandbox URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/2.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

schema_view = get_swagger_view(title='Civic Sandbox APIs')

urlpatterns = [
    path('sandbox/', schema_view),
    path('sandbox/', include('registry.urls')),
    path('sandbox/neighborhood-development/', include('neighborhood_development_18.urls')),
    path('sandbox/transportation-systems/', include('transportation_systems_18.urls')), 
    path('sandbox/disaster-resilience/', include('disaster_resilience_18.urls')), 
    path('sandbox/housing-affordability/', include('housing_affordability_18.urls')), 

]
