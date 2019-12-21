from django.shortcuts import render
from db_manager.utils import database_upload

def db_upload(request):
    """ Uncomment if refreshing data needed"""
    # database_upload()
    return render(request, 'index.html')
