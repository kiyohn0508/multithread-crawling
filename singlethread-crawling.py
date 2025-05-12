import pathlib
import requests
from bs4 import BeautifulSoup
import time

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
        get_topic_contents(new_url)

start = time.perf_counter()

url = 'https://news.hada.io/'

get_topics(url)

end = time.perf_counter()
print(f"모든 작업 완료! {end-start:.4f}")

