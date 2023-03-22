import typing

from restaurant_monitoring.dtos import StoreDTO, StoreBusinessHourDTO, StoreMenuHourDTO
from restaurant_monitoring.models import Store, StoreBusinessHour, StoreMenuHour


def create_stores(list_of_store_dtos: typing.List[StoreDTO]):
    list_of_objs = [
        Store(
            store_id=each.store_id,
            timezone=each.timezone
        )
        for each in list_of_store_dtos
    ]
    Store.objects.bulk_create(list_of_objs)


def create_store_business_hour(list_of_store_status_dtos: typing.List[StoreBusinessHourDTO]):
    list_of_objs = [
        StoreBusinessHour(
            store_id=int(each.store_id),
            status=each.status,
            timestamp_utc=each.timestamp_utc,
        )
        for each in list_of_store_status_dtos
    ]
    StoreBusinessHour.objects.bulk_create(list_of_objs)


def create_store_menu_hour(list_of_store_menu_hour_dtos: typing.List[StoreMenuHourDTO]):
    list_of_objs = [
        StoreMenuHour(
            store_id=int(each.store_id),
            day_of_week=each.day_of_week,
            start_time=each.start_time,
            end_time=each.end_time
        )
        for each in list_of_store_menu_hour_dtos
    ]

    StoreMenuHour.objects.bulk_create(list_of_objs)
