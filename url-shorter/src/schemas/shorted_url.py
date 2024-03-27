from models.shorted_url import ShortedUrl
from pydantic import parse_obj_as


def individual_serial(shorted_url: dict) -> ShortedUrl | None:
    print(shorted_url)
    if shorted_url is not None:
        shorted_url = {str(key): str(value) for key, value in shorted_url.items()}
        return parse_obj_as(ShortedUrl, shorted_url)
    else:
        return None


def list_serial(shorted_urls: list[dict]) -> list[ShortedUrl]:
    return [individual_serial(shorted_url) for shorted_url in shorted_urls]
