import requests
from bs4 import BeautifulSoup
import time
import threading

threads = []

def get_topic_contents(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    contents = soup.select('#topic_contents')

    print(contents)

def get_topics(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles =  soup.select('.topicdesc')

    for title in titles:
        sp_url = title.find('a').get('href')
        new_url = url+sp_url
        start_threads(new_url)
        
    finish_threads(threads)

def start_threads(url):
    t = threading.Thread(target=get_topic_contents, args=(url,))
    t.start()
    threads.append(t)

def finish_threads(threads):
    for t in threads:
        t.join()
    

start = time.perf_counter()

url = 'https://news.hada.io/'

get_topics(url)

end = time.perf_counter()
print(f"모든 멀티쓰레드 작업 완료! {end-start:.4f}")

