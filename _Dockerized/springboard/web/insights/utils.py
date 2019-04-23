from data.utils import springboard_clean_path, springboard_mlb_path
import pandas as pd
from apyori import apriori


def statistical_data():
    dataset = pd.read_csv(springboard_clean_path)
    skills_mlb = pd.read_csv(springboard_mlb_path)

    # top providers

    occurence = dataset['provider'].value_counts()[:6]
    top_providers_dict = occurence.to_dict()

    # ECTS Credits breakdown

    dataset['less_than_50'] = dataset['ects_credits'].apply(
        lambda x: 'below 50 C' if x < 50 else 'over 50 C')
    less_than_50_values = dataset['less_than_50'].value_counts()
    lt50_dict = less_than_50_values.to_dict()

    # partime/ fulltime

    mode_values = dataset['mode'].value_counts()
    mode_dict = mode_values.to_dict()

    # NFQ

    nfq_values = dataset['nfq'].value_counts()
    nfq_dict = nfq_values.to_dict()

    # Top popular categories

    skill_total = skills_mlb.iloc[:, :].sum(axis=0).sort_values(ascending=False)[:6]

    skill_dict = skill_total.to_dict()

    stats_dict = {"top_providers_dict": top_providers_dict,
                  "lt50_dict": lt50_dict,
                  "nfq_dict": nfq_dict,
                  "mode_dict": mode_dict,
                  "skill_dict": skill_dict,
                  }

    return stats_dict


def insights_data():
    dataset = pd.read_csv(springboard_clean_path)
    skills_mlb = pd.read_csv(springboard_mlb_path)

    # Master/bachelor/other award

    masters = ['Master', 'Msc', 'master', 'msc']
    bachelors = ['Bachelor', 'bachelor', 'bsc', 'Bsc']

    dataset['masters'] = dataset['title'].apply(lambda x: 1 if any(w in x for w in masters) else 0)
    dataset['bachelors'] = dataset['title'].apply(lambda x: 1 if any(w in x for w in bachelors) else 0)

    dataset_masters = dataset[(dataset['masters'] == 1)]
    dataset_masters = dataset_masters.iloc[:, :12]
    dataset_bachelors = dataset[(dataset['bachelors'] == 1)]
    dataset_bachelors = dataset_bachelors.iloc[:, :12]
    dataset_others = dataset[(dataset['masters'] == 0) & (dataset['bachelors'] == 0)]
    dataset_others = dataset_others.iloc[:, :12]

    # DATES

    # closest deadline

    closest_deadline = dataset.sort_values(by=['deadline'])[:6]
    closest_deadline_courses = closest_deadline.iloc[:, :11]
    closest_deadline_courses_list = closest_deadline_courses.values.tolist()

    # top 6 shortest masters

    dataset_masters['start_date'] = pd.to_datetime(dataset_masters['start_date']).dt.date
    dataset_masters['end_date'] = pd.to_datetime(dataset_masters['end_date']).dt.date

    dataset_masters['duration'] = (dataset_masters['end_date'] - dataset_masters['start_date']).astype(
        'timedelta64[D]').astype(int)
    dataset_masters = dataset_masters.sort_values(['duration'])[:6]
    dataset_masters_list = dataset_masters.values.tolist()

    # top 6 shortest bachelors

    dataset_bachelors['start_date'] = pd.to_datetime(dataset_bachelors['start_date']).dt.date
    dataset_bachelors['end_date'] = pd.to_datetime(dataset_bachelors['end_date']).dt.date
    dataset_bachelors['duration'] = (dataset_bachelors['end_date'] - dataset_bachelors['start_date']).astype(
        'timedelta64[D]').astype(int)
    dataset_bachelors = dataset_bachelors.sort_values(['duration'])[:6]
    dataset_bachelors_list = dataset_bachelors.values.tolist()

    # top 6 shortest others

    dataset_others['start_date'] = pd.to_datetime(dataset_others['start_date']).dt.date
    dataset_others['end_date'] = pd.to_datetime(dataset_others['end_date']).dt.date
    dataset_others['duration'] = (dataset_others['end_date'] - dataset_others['start_date']).astype(
        'timedelta64[D]').astype(int)
    dataset_others = dataset_others.sort_values(['duration'])[:6]
    dataset_others_list = dataset_others.values.tolist()

    insights_dict = {"closest_deadline_courses_list": closest_deadline_courses_list,
                     "dataset_masters_list": dataset_masters_list,
                     "dataset_bachelors_list": dataset_bachelors_list,
                     "dataset_others_list": dataset_others_list,
                     }

    return insights_dict

def apply_apriori():
    """Associated Rule Learning Algorithm"""
    dataset = pd.read_csv(springboard_clean_path)

    rows = len(dataset)

    dataset = pd.DataFrame(dataset['skills'].str.split().values.tolist())

    # Preparing ARR skill list

    skills = []
    for i in range(0, rows):
        skills.append([str(dataset.values[i, j]) for j in range(0, 4)])

    # Training Apriori on the dataset

    rules = apriori(skills, min_support=0.3, min_confidence=0.5, min_lift=2, min_length=2)

    results = list(rules)

    rules_list = []
    for i in range(0, len(results)):
        result = results[i]
        supp = round(result.support, 4) * 100
        supp = str(supp)[:5] + '%'
        conf = int(result.ordered_statistics[0].confidence * 100)
        lift = round(result.ordered_statistics[0].lift, 3)
        hypo = ''.join([x + ' ' for x in result.ordered_statistics[0].items_base])
        hypo = str(hypo)
        hypo = hypo.replace('None','')
        conc = ''.join([x + ' ' for x in result.ordered_statistics[0].items_add])
        conc = str(conc)
        # conc = conc.replace('.','')
        rule = [hypo, str(conf), conc, str(supp), str(lift)]
        rules_list.append(rule)

    apriori_dict = {"apriori_rules": rules_list}

    return apriori_dict
















