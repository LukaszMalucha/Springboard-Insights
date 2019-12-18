from django.shortcuts import render


def db_upload(request):
    """ Uncomment if refreshing data needed"""
    # database_upload()
    return render(request, 'index.html')
