from django.core.management.base import BaseCommand
import pandas as pd
from restaurant_monitoring.dtos import StoreDTO
from restaurant_monitoring.storages import storage_implementation as storage
from csv import DictReader


class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open("stores.csv", 'r') as f:
            dict_reader = DictReader(f)

            list_of_dict = list(dict_reader)
            list_of_store_dtos = []
            for each in list_of_dict:
                timezone_str = "America/Chicago"
                store_id = each["store_id"]
                if timezone_str:
                    timezone_str = each["timezone_str"]

                list_of_store_dtos.append(
                    StoreDTO(
                        store_id=store_id,
                        timezone=timezone_str
                    )
                )

            storage.create_stores(list_of_store_dtos)










