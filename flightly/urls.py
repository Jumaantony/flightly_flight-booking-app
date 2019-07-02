"""flightly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from flightly.helpers.scheduler.jobs import scheduler
from django.contrib import admin
from django.urls import path, include
from django.conf import settings


admin.site.site_header = "Flightly Admin"
admin.site.site_title = "Flightly Admin Portal"
admin.site.index_title = "Welcome to Flightly Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('api/v1/', include('flightly.users.urls')),
    path('api/v1/', include('flightly.flight_booking.urls')),
    path('', include('flightly.docs.urls')),
]


# Starting Background Scheduler
if settings.SCHEDULER_AUTOSTART:
    scheduler.start()
