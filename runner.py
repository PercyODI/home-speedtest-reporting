import speedtest
import json
import time

while 1:
    servers = []

    try:
        s = speedtest.Speedtest()
        s.get_servers(servers)
        s.get_best_server()

        s.download(threads=1)
    except:
        print('Failed for reasons, trying again')
        time.sleep(5)
        continue
    results = s.results.dict()
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
