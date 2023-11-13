from dataclasses import dataclass, asdict

@dataclass
class Foo:
    val: str

f = Foo(val='a')
print(asdict(f))

from datetime import datetime, timedelta
import time

def get_epoch_start():
    # https://docs.python.org/3/library/time.html#time.struct_time
    time_struct = time.gmtime(0)
    return datetime(year=time_struct.tm_year, month=time_struct.tm_mon, day=time_struct.tm_mday)

def millisecond_to_datetime(ms):
    return get_epoch_start() + timedelta(milliseconds=ms)

exp_epoch = datetime

exp_epoch =  get_epoch_start() + timedelta(milliseconds=1719561600000)
epoch_now = datetime.now()

time_diff: timedelta = exp_epoch - epoch_now
diff_in_days = time_diff.days 

print(exp_epoch)
print(epoch_now)
print(diff_in_days)

