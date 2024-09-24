import time
import threading


def beat_interval(delay_ms: int, function, blocking: bool = False) -> None:
    def wrapper():
        while True:
            function()
            time.sleep(delay_ms / 1000)

    t = threading.Thread(target=wrapper)

    t.start()

    if blocking:
        t.join()
