import datetime


def change_date(date):
    x = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
    new_date = x.strftime("%a, %d %b %Y %H:%M:%S")
    return new_date


def change_date_for_cache(date):
    x = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
    new_date = x.strftime("%Y%m%d")
    return new_date

