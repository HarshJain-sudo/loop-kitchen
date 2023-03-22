import typing

from restaurant_monitoring.dtos import StoreDTO
from restaurant_monitoring.models import Store


def create_stores(list_of_store_dtos: typing.List[StoreDTO]):
    list_of_objs = [
        Store(
            store_id=each.store_id,
            timezone=each.timezone
        )
        for each in list_of_store_dtos
    ]
    Store.objects.bulk_create(list_of_objs)
