import pytz
from django.core.management.base import BaseCommand
import uuid
from restaurant_monitoring.dtos import StoreDTO, StoreBusinessHourDTO
from restaurant_monitoring.storages import storage_implementation as storage
from csv import DictReader
from datetime import datetime


class Command(BaseCommand):
    help = 'import booms'

    @staticmethod
    def generate_uuid():
        return str(uuid.uuid4())

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open("storestatus.csv", 'r') as f:
            dict_reader = DictReader(f)

            list_of_dict = list(dict_reader)

            list_of_store_status_dtos = []
            for each in list_of_dict:
                timezone = pytz.timezone('UTC')
                list_of_store_status_dtos.append(
                    StoreBusinessHourDTO(
                        store_id="{:.0f}".format(float(each['store_id'])),
                        status=each['status'],
                        timestamp_utc=timezone.localize(
                            datetime.strptime(each['timestamp_utc'], '%Y-%m-%d %H:%M:%S.%f %Z')
                        )
                    )
                )

            storage.create_store_statuses(list_of_store_status_dtos)










