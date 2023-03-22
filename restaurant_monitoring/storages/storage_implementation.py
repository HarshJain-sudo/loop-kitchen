import typing

from restaurant_monitoring.dtos import StoreDTO, StoreStatusDTO
from restaurant_monitoring.models import Store, StoreStatus


def create_stores(list_of_store_dtos: typing.List[StoreDTO]):
    list_of_objs = [
        Store(
            store_id=each.store_id,
            timezone=each.timezone
        )
        for each in list_of_store_dtos
    ]
    Store.objects.bulk_create(list_of_objs)


def create_store_statuses(list_of_store_status_dtos: typing.List[StoreStatusDTO]):
    list_of_objs = [
        StoreStatus(
            id=each.id,
            store_id=each.store_id,
            status=each.status,
            timestamp_utc=each.timestamp_utc,
        )
        for each in list_of_store_status_dtos
    ]
    StoreStatus.objects.bulk_create(list_of_objs)
