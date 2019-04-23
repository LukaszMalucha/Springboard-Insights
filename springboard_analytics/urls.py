from django.contrib import admin
from django.urls import path, include

from django.conf.urls import handler404, handler500
from dashboard.views import error_404, error_500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('user/', include('user.urls')),
    path('data/', include('data.urls')),
    path('insights/', include('insights.urls')),
    path('api/', include('api.urls')),
]


handler404 = error_404
handler500 = error_500