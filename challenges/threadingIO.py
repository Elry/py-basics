import time
from concurrent.futures import ThreadPoolExecutor

def fetch_urls(url):
    print(f'Start fetching {url}')
    time.sleep(2) # API response latency
    return f'Done {url}'

urls = ["site1.com", "site2.com", "site3.com"]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(fetch_urls, urls))

print(results)

