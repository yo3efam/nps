import json
from typing import List
import datetime
from .control.beat import beat_interval
from .udp.client import send_message
from . import config as cfg


def register_server(notif_host: str, notif_port: int, key: str, server_name: str):
    cfg.REGION = server_name
    cfg.KEY = key
    cfg.HOST = notif_host
    cfg.PORT = notif_port

    def beat():
        routes = []
        for channel_name in cfg.buffer_channels:
            routes.append(cfg.buffer_channels[channel_name])
        data = {
            "name": server_name,
            "key": key,
            "routes": routes,
            "date": (datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds(),
        }
        message = {
            "type": "region_beat",
            "data": data
        }
        send_message(notif_host, notif_port, json.dumps(message))

    beat_interval(5_000, beat)
