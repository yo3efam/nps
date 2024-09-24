import json
from typing import List
from .utils.security import create_sign
from .utils.crypto import notif_hmac
from . import config as cfg
import datetime
from .udp.client import send_message


def create_permission(username: str, user_id: str, allowed_routes: List[str]) -> dict:
    date = (datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds()
    sign = create_sign(username, user_id, date, allowed_routes)

    return {
        "region": cfg.REGION,
        "name": username,
        "uid": user_id,
        "allowed_routes": allowed_routes,
        "date": date,
        "sign": sign,
    }


def register_channel(channel: str, stash_lifetime_seconds: int) -> None:
    cfg.buffer_channels.update({channel: {"name": channel, "stash_sec": stash_lifetime_seconds}})
    # message = {
    #     "type": "register_channel",
    #     "data": {
    #         "region": cfg.REGION,
    #         "channel": channel,
    #         "stash_sec": stash_lifetime_seconds,
    #         "sign": notif_hmac(f"{cfg.REGION}|{stash_lifetime_seconds}|{channel}", cfg.KEY)
    #     },
    # }
    # send_message(cfg.HOST, cfg.PORT, json.dumps(message))


def destroy_channel(channel: str) -> None:
    del cfg.buffer_channels[channel]
    # message = {
    #     "type": "destroy_channel",
    #     "data": {
    #         "region": cfg.REGION,
    #         "channel": channel,
    #         "sign": notif_hmac(f"{cfg.REGION}|{channel}", cfg.KEY)
    #     },
    # }
    # send_message(cfg.HOST, cfg.PORT, json.dumps(message))


def notify(route: str, data: str) -> None:
    message = {
        "type": "notify",
        "data": {
            "region": cfg.REGION,
            "route": route,
            "data": data,
            "sign": notif_hmac(f"{cfg.REGION}|{route}|{data}", cfg.KEY)
        },
    }
    send_message(cfg.HOST, cfg.PORT, json.dumps(message))


def notify_users(user_uids: List[str], data: str) -> None:
    user_str = "".join([u for u in user_uids])
    message = {
        "type": "notify_target",
        "data": {
            "region": cfg.REGION,
            "users": user_uids,
            "data": data,
            "sign": notif_hmac(f"{cfg.REGION}|{user_str}|{data}", cfg.KEY)
        },
    }
    send_message(cfg.HOST, cfg.PORT, json.dumps(message))
