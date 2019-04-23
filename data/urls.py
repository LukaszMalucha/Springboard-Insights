from django.urls import path
from data import views

app_name = 'data'

urlpatterns = [
    path('', views.preprocessing, name='preprocessing'),
    path('data_extraction', views.data_extraction, name='data_extraction'),
    path('data_featurization', views.data_featurization, name='data_featurization'),
    path('data_upload', views.data_upload, name='data_upload'),
    ]