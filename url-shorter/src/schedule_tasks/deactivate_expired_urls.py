import datetime
from typing import List

from db.database import collection_name
from models.shorted_url import ShortedUrl, UpdateShortedUrl
from schemas.shorted_url import list_serial
from services.shorted_url import update_su


def deactivate_expiring_urls() -> None:
    current_date = datetime.datetime.utcnow()

    short_urls: List[ShortedUrl] = list_serial(collection_name.find({
        "$and": [
            {"expire_at": {"$lt": current_date}},
            {"is_active": True}
        ]
    }))

    [update_su(short_url.id, set_expire(short_url)) for short_url in short_urls]


def set_expire(shorted_url: ShortedUrl) -> UpdateShortedUrl:
    shorted_url.is_active = False
    return shorted_url.convert_to_update_model()
