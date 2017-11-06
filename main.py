import csv
import urllib.parse
import urllib.request
import time
from bs4 import BeautifulSoup

row_names = ['movie_id', 'movie_title']
with open('u.item.txt', 'r', encoding = "ISO-8859-1") as f:
    reader = csv.DictReader(f, fieldnames=row_names, delimiter='|')
    for row in reader:
        movie_id = row['movie_id']
        movie_title = row['movie_title']
        url = 'http://www.imdb.com/find?q=' + urllib.parse.quote_plus(movie_title)
        with urllib.request.urlopen(url) as response:
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            print(soup.prettify())
        time.sleep(1)
