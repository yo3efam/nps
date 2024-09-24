import hashlib
import hmac


def notif_hmac(data: str, key: str) -> str:
    return hmac.new(key.encode("utf8"), data.encode("utf8"), hashlib.sha256).hexdigest()
