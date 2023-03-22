from django.urls import path
from .views import trigger_report_view, get_report_view

urlpatterns = [
    path('trigger_report/', trigger_report_view, name='trigger_report'),
    path('get_report/<int:report_id>/', get_report_view, name='get_report')
]
