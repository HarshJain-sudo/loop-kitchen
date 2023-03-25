from django.http import JsonResponse
from restaurant_monitoring.storages import storage_implementation as storage
from restaurant_monitoring import utils


def trigger_report_view(request):
    business_hours_dict = storage.get_business_hour_dict()

    store_ids = [
        each['store_id']
        for each in business_hours_dict
    ]

    menu_hour_dict = storage.get_menu_hour_dict(
        store_ids)

    business_hours = utils.prepare_dict_for_menu_hours(
        menu_hour_dict)

    response = {
        'report_id': business_hours
    }
    return JsonResponse(response)


def get_report_view(request, report_id):
    report_data = {'id': report_id, 'data': 'Example report data'}
    return JsonResponse(report_data)
