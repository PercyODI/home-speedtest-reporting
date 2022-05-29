import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import json
from dateutil import parser

results = []

with open("dst/results.json", "r") as f_handle:
    for line in f_handle.readlines():
        results.append(json.loads(line))
y_vals = list(map(lambda x: x["download_mbps"], results))
x_vals = list(map(lambda x: parser.parse(x["timestamp"]), results))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y %I:%M:%S %p'))

plt.setp(plt.gca().get_xticklabels(), rotation=30, ha='right')
plt.tight_layout()

plt.plot(x_vals, y_vals)
plt.show()
