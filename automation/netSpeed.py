# Internet Speed tester
# pip install speedtest-cli
import speedtest

# Set Best st
st = speedtest.S
st.get_best_server()

download_speed = st.download() / 1_000_000  # Convert to Mbps
upload_speed = st.upload() / 1_000_000  # Convert to Mbps
ping = st.results.ping

print(f"Ping Speed: {ping}")
print(f"Download Speed: {download_speed:.2f} Mbps")
print(f"Upload Speed: {upload_speed:.2f} Mbps")
