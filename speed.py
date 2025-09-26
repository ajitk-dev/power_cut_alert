import time
from datetime import datetime
import speedtest

def test_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000      # Convert to Mbps
    ping = st.results.ping
    return download_speed, upload_speed, ping

def log_speed(interval=5):  # every 5 seconds
    while True:
        try:
            download, upload, ping = test_speed()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{timestamp}] Download: {download:.2f} Mbps | Upload: {upload:.2f} Mbps | Ping: {ping:.2f} ms")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(interval)

if __name__ == "__main__":
    try:
        log_speed(interval=5)
    except KeyboardInterrupt:
        print("\nSpeed test logging interrupted by user. Exiting gracefully...")
