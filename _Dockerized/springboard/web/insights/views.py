from django.shortcuts import render
from pathlib import Path

from data.utils import springboard_clean_path, springboard_mlb_path
from insights.utils import statistical_data, insights_data, apply_apriori


def statistics(request):
    dataset_clean = Path(springboard_clean_path)
    dataset_mlb = Path(springboard_mlb_path)

    if (dataset_mlb.is_file() and dataset_clean.is_file()):
        context = statistical_data()
        context['phase'] = 'mlb_ready'



    else:
        context = {'phase': 'data_preprocessing'}

    return render(request, "statistics.html", context)


def insights(request):

    dataset_clean = Path(springboard_clean_path)
    dataset_mlb = Path(springboard_mlb_path)

    if (dataset_mlb.is_file() and dataset_clean.is_file()):
        context = insights_data()
        context['phase'] = 'mlb_ready'



    else:
        context = {'phase': 'data_preprocessing'}

    return render(request, "insights.html", context)



def apriori_algorithm(request):

    dataset_clean = Path(springboard_clean_path)
    dataset_mlb = Path(springboard_mlb_path)

    if (dataset_mlb.is_file() and dataset_clean.is_file()):
        context = apply_apriori()
        context['phase'] = 'mlb_ready'

    else:
        context = {'phase': 'data_preprocessing'}




    return render(request, "apriori.html", context)
















