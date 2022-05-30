import speedtest
from speedtest import SpeedtestHTTPError, ServersRetrievalError
import json
import time
from datetime import datetime, timezone

while 1:
    servers = [1]

    try:
        s = speedtest.Speedtest()
        # s.get_servers(servers)
        s.get_best_server()

        s.download(threads=1)
        results = s.results.dict()
    except (SpeedtestHTTPError) as e:
        print("Got an error, think it's a no connection")
        print(e)
        results = {
            "download": 0,
            "ping": 0,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
    except:
        print(
            "Failed for reasons, don't think it connection, not recording, and trying again"
        )
        time.sleep(5)
        continue
    result_str = json.dumps(
        {
            "download_bps": results["download"],
            "download_mbps": float(results["download"]) * 9.536743e-7,
            "ping": results["ping"],
            "timestamp": results["timestamp"],
        }
    )

    print(result_str)
    with open("dst/results.json", "a") as f_handle:
        f_handle.write(result_str + "\n")
    time.sleep(5)
