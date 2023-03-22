import typing

from restaurant_monitoring.dtos import StoreDTO, StoreBusinessHourDTO
from restaurant_monitoring.models import Store, StoreBusinessHour


def create_stores(list_of_store_dtos: typing.List[StoreDTO]):
    list_of_objs = [
        Store(
            store_id=each.store_id,
            timezone=each.timezone
        )
        for each in list_of_store_dtos
    ]
    Store.objects.bulk_create(list_of_objs)


def create_store_statuses(list_of_store_status_dtos: typing.List[StoreBusinessHourDTO]):
    list_of_objs = [
        StoreBusinessHour(
            store_id=int(each.store_id),
            status=each.status,
            timestamp_utc=each.timestamp_utc,
        )
        for each in list_of_store_status_dtos
    ]
    StoreBusinessHour.objects.bulk_create(list_of_objs)
