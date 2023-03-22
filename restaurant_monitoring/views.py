from django.shortcuts import render
from django.http import JsonResponse


def trigger_report_view(request):
    report_id = 123
    return JsonResponse({'report_id': report_id})


def get_report_view(request, report_id):
    report_data = {'id': report_id, 'data': 'Example report data'}
    return JsonResponse(report_data)
