from django.urls import path
from insights import views

app_name = 'insights'

urlpatterns = [
    path('statistics', views.statistics, name='statistics'),
    path('insights', views.insights, name='insights'),
    path('apriori', views.apriori_algorithm, name='apriori'),
    ]