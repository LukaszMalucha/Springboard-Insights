from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from pathlib import Path

from data.utils import dataset_preprocessing, springboard_clean_path, springboard_scrape_path, mlb_vizualization, \
    springboard_mlb_path, data_extractor, data_visualization, data_binarizer, database_upload


def preprocessing(request):
    dataset_raw = Path(springboard_scrape_path)
    dataset_clean = Path(springboard_clean_path)
    dataset_mlb = Path(springboard_mlb_path)

    if (dataset_raw.is_file() and dataset_clean.is_file()):

        context = data_visualization()
        context['phase'] = 'data_preprocessing'

        if dataset_mlb.is_file():
            mlb_data = mlb_vizualization()
            context['skill_clean'] = mlb_data.to_html()
            context['phase'] = 'mlb_ready'

    else:

        context = dict()
        context['phase'] = 'data_extraction'

    return render(request, "data_preprocessing.html", context)


def data_extraction(request):
    """Run WebCrawler"""
    data_extractor()
    dataset_preprocessing()
    messages.success(request, "Data Extraction Sucessful")
    return redirect(reverse('data:preprocessing'))


def data_featurization(request):
    """Preparing skill column for for ARR algorithm"""
    data_binarizer()
    messages.success(request, "Data Featurization Successful")

    return redirect(reverse('data:preprocessing'))


def data_upload(request):
    """Uploading recent course data to DB"""
    database_upload()
    messages.success(request, "Data Upload Successful")

    return redirect(reverse('data:preprocessing'))
