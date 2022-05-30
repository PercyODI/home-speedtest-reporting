import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import json
from dateutil import parser
import pytz

results = []
my_timezone = pytz.timezone("America/Chicago")

with open("dst/results.json", "r") as f_handle:
    for line in f_handle.readlines():
        results.append(json.loads(line))
download_bpss = list(map(lambda x: x["download_bps"], results))
pings = list(map(lambda x: x["ping"], results))
timestamps = list(map(lambda x: parser.parse(x["timestamp"]), results))

plt.figure()
plt.subplot(211)
plt.title('Download Speed')
plt.gca().xaxis.set_major_formatter(
    mdates.DateFormatter("%m/%d/%Y %I:%M:%S %p", tz=my_timezone)
)
plt.gca().xaxis.set_visible(False)
plt.gca().axhline(0, color="red")

# (None))#.get_xticklabels(), rotation=30, ha='right')

plt.plot(timestamps, download_bpss)

plt.subplot(212)
plt.title('Ping')
plt.gca().xaxis.set_major_formatter(
    mdates.DateFormatter("%m/%d/%Y %I:%M:%S %p", tz=my_timezone)
)
plt.setp(plt.gca().get_xticklabels(), rotation=30, ha="right")
plt.gca().axhline(0, color="red")

plt.plot(timestamps, pings)

plt.tight_layout()

plt.show()
