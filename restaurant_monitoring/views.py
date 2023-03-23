from django.http import JsonResponse
from datetime import datetime, timedelta
from .models import StoreBusinessHour, Store
from .utils import get_report_data
from restaurant_monitoring.storages import storage_implementation as storage


def trigger_report_view(request):
    store_dtos = storage.get_all_stores()
    store_ids = [
        each.store_id
        for each in store_dtos
    ]

    store_menu_hour_dict = storage.get_menu_hour_dict(store_ids)

    store_menu_hour_ids = [
        each['store_id']
        for each in store_menu_hour_dict
    ]

    store_business_hour_dict = storage.get_business_hour_dict(store_menu_hour_ids)
    response = {
        "store_menu_hour_dict": store_menu_hour_dict,
        "store_business_hour_dict": store_business_hour_dict
    }
    return JsonResponse(response)


def get_report_view(request, report_id):
    report_data = {'id': report_id, 'data': 'Example report data'}
    return JsonResponse(report_data)
