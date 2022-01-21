import requests
import time
from bs4 import BeautifulSoup
import concurrent.futures
import csv
import threading
csv_writer_lock = threading.Lock()

base_url = 'https://www.4byte.directory/signatures/?page={}'

sigs = set()
run_time =0


def save(fn, lsig):
    end = False
    with csv_writer_lock:
        with open(fn, mode='a',newline='') as f:
            writer = csv.writer(f)
            # print(lsig[0])
            for s in lsig:
                if s not in sigs:
                    sigs.add(s)
                    
                    # print(type(s))
                    # f.write(f"{s[0]} := {s[1]}: {s[2]}\n")
                    writer.writerow(s)
                    f.flush()
                else:
                    end = True
        
    return end

urls = []
for i in range(1,42325):
    url = base_url.format(i)
    urls.append(url)

# print(len(urls))

save_file = 'Parsed.csv'

MAX_THREADS = 30

def download_url(url):
    # print(url)
    # resp = requests.get(url)
    r = requests.get(url).content
    r = BeautifulSoup(r,features="lxml")
    hashes = [x.text for x in r.find_all('td', class_='bytes_signature')]
    names = [x.text for x in r.find_all('td', class_='text_signature')]
    ids = [x.text for x in r.find_all('td',class_='id')]
    
    ed = save(save_file,list(zip(ids,hashes, names)))
    if ed:
        return
    
        
    
    
def download_pages(page_urls):
    threads = min(MAX_THREADS, len(page_urls))
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(download_url, page_urls)



def main(page_urls):
    t0 = time.time()
    download_pages(page_urls)
    
    t1 = time.time()
    print(f"{t1-t0} seconds to parse {len(page_urls)} pages.")

main(urls)
