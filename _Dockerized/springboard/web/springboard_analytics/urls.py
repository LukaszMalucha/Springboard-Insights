from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('user/', include('user.urls')),
    path('data/', include('data.urls')),
    path('insights/', include('insights.urls')),
    path('api/', include('api.urls')),
]
