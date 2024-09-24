from typing import List
from .crypto import notif_hmac
from .. import config as cfg


def create_sign(user_name: str, uid: str, date: int, allowed_routes: List[str]) -> str:
    routes_str = "".join([r for r in allowed_routes])
    data_str = f"{cfg.REGION}|{uid}|{user_name}|{date}|{routes_str}"
    return notif_hmac(data_str, cfg.KEY)
