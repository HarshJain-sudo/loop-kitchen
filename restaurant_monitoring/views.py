from django.http import JsonResponse
from datetime import datetime, timedelta
from .models import StoreBusinessHour, Store
from .utils import get_report_data


def trigger_report_view(request):
    # Get the latest timestamp from the database
    all_store_ids = Store.objects.all().value_list('store_id', flat=True)

    latest_timestamp = StoreBusinessHour.objects.filter(store_id__in=all_store_ids).latest('timestamp_utc').timestamp_utc

    # Set the current timestamp to the latest timestamp in the database
    current_timestamp = latest_timestamp

    # Set the start and end times for the report (last hour, last day, last week)
    end_time_last_hour = current_timestamp
    start_time_last_hour = end_time_last_hour - timedelta(hours=1)

    end_time_last_day = current_timestamp
    start_time_last_day = end_time_last_day - timedelta(days=1)

    end_time_last_week = current_timestamp
    start_time_last_week = end_time_last_week - timedelta(weeks=1)

    # Get the report data
    report_id = get_report_data(
        start_time_last_hour,
        end_time_last_hour,
        start_time_last_day,
        end_time_last_day,
        start_time_last_week,
        end_time_last_week
    )

    return JsonResponse({'report_id': report_id})


def get_report_view(request, report_id):
    report_data = {'id': report_id, 'data': 'Example report data'}
    return JsonResponse(report_data)
