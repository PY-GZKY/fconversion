import getpass
import time
import uuid
from datetime import datetime

from dateutil import tz

from src.constants import TIME_ZONE


def get_user_name():
    return getpass.getuser()


def gen_uuid():
    return str(uuid.uuid4())


def as_int(f: float) -> int:
    return int(round(f))


def timestamp_ms() -> int:
    return as_int(time.time() * 1000)


def ms_to_datetime(unix_ms: int) -> datetime:
    tz_ = tz.gettz(TIME_ZONE)
    return datetime.fromtimestamp(unix_ms / 1000, tz=tz_)


def to_str_datetime():
    return datetime.now().strftime('%Y-%m-%d_%H%M%S%f')
