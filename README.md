# MovieLens 100K Posters
Links to posters of movies in the [MovieLens 100K dataset](https://grouplens.org/datasets/movielens/100k/). The links were scraped from [IMDb](http://www.imdb.com/). The posters are mapped to the movie_id in the dataset. The IMDB URLs of the movies are also present.

## Description of files
- [movie_poster.csv](https://github.com/babu-thomas/movielens-posters/blob/master/movie_poster.csv): The movie_id to poster URL mapping.
- [movie_poster.py](https://github.com/babu-thomas/movielens-posters/blob/master/movie_poster.py): The script used for scraping the poster URLs.
- [movie_url.csv](https://github.com/babu-thomas/movielens-posters/blob/master/movie_url.csv): The movie_id to IMDb URL mapping.
- [movie_url.py](https://github.com/babu-thomas/movielens-posters/blob/master/movie_url.py): The script used for scraping the IMDb URLs.
- [u.item.txt](https://github.com/babu-thomas/movielens-posters/blob/master/u.item.txt):  Movie details from the dataset. The full dataset and its details can be found [here](https://grouplens.org/datasets/movielens/100k/).

## Running it yourself
You will need Python 3 and [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/).
- Install Beautiful Soup: `pip install beautifulsoup4`
- Scrape IMDb URLs: `python3 movie_url.py`
- Scrape poster URLs: `python3 movie_poster.py`
