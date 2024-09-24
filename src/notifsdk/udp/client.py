import socket


def send_message(host: str, port: int, data: str) -> None:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(data.encode("utf8"), (host, port))
