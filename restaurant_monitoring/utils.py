import itertools


def prepare_dict_for_menu_hours(menu_hour_dict):

    DAYS_OF_WEEK = [0, 1, 2, 3, 4, 5, 6]
    store_ids = [
        each['store_id']
        for each in menu_hour_dict
    ]

    business_hours = {store_id: {day_of_week: (None, None) for day_of_week in DAYS_OF_WEEK} for store_id in store_ids}

    for hours in menu_hour_dict:
        store_id = hours['store_id']
        day_of_week = hours['day_of_week']
        start_time = hours['start_time']
        end_time = hours['end_time']
        business_hours[store_id][day_of_week] = (start_time, end_time)

    return business_hours



