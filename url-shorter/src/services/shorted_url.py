import hashlib

from datetime import datetime, timedelta

from bson import ObjectId
from pydantic import parse_obj_as, HttpUrl
from pymongo import ReturnDocument

from core.config import app_settings
from db.database import collection_name
from models.shorted_url import ShortedUrl, UpdateShortedUrl
from schemas.shorted_url import list_serial, individual_serial


def get_su() -> list[ShortedUrl]:
    short_urls = list_serial(collection_name.find())
    return short_urls


def get_su_by_shorted(shorted: str) -> ShortedUrl | None:
    short_url = individual_serial(collection_name.find_one({"shorted": shorted}))
    return short_url


def create_su(user_id: int, url_to_short: HttpUrl) -> ShortedUrl:
    shorted_url = {
        "origin": str(url_to_short),
        "user_id": user_id,
        "shorted": create_short_url(url_to_short, user_id),
        "is_active": True,
        "count_of_visits": 0,
        "expire_at": datetime.utcnow() + timedelta(days=app_settings.short_url_expire_days)
    }

    created_id = str(collection_name.insert_one(shorted_url).inserted_id)
    shorted_url["id"] = created_id
    return parse_obj_as(ShortedUrl, shorted_url)


def update_su(short_url_id: str, short_url: UpdateShortedUrl) -> ShortedUrl:
    updated_url = collection_name.find_one_and_update({"_id": ObjectId(short_url_id)},
                                                      {"$set": dict(short_url)},
                                                      return_document=ReturnDocument.AFTER)
    return parse_obj_as(ShortedUrl, updated_url)


def delete_su(short_url_id: str) -> dict[str, int]:
    del_count = collection_name.delete_one({"_id": ObjectId(short_url_id)})
    return {"deleted_count": del_count.deleted_count}


def create_short_url(origin: HttpUrl,
                     user_id: int,
                     length: int = app_settings.base_short_url_length) -> str:
    hash_origin = hashlib.sha256(str(origin).encode())
    hashed_origin = hash_origin.hexdigest()
    return hashed_origin[:length] + str(user_id)
