from dataclasses import dataclass
from datetime import datetime


@dataclass
class StoreDTO:
    store_id: str
    timezone: str


@dataclass
class StoreStatusDTO:
    id: str
    store_id: str
    status: str
    timestamp_utc: datetime


@dataclass
class StoreMenuHourDTO:
    id: str
    store_id: str
    day_of_week: int
    start_time: datetime
    end_time: datetime
