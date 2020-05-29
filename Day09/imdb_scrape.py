import json
import urllib.request
from bs4 import BeautifulSoup
import requests
import pandas as pd


def get_movie_ids(num=30, page=1):
    links_data = pd.read_csv("./scrape_imdb/links.csv")
    movie_ids = list(links_data.imdbId)
    start_index = (page - 1) * num
    end_index = start_index + num
    return movie_ids[start_index:end_index]


def scrape_index_page(movie_id):
    movie_index_url = "https://www.imdb.com/title/tt{}/".format(str(movie_id).zfill(7))
    current_page = requests.get(movie_index_url)
    index_soup = BeautifulSoup(current_page.text, "html.parser")
    current_page_json = index_soup.find("script", attrs={"type": "application/ld+json"})
    current_page_json = str(current_page_json)[str(current_page_json).find('{'):-9]
    return current_page_json


def collect_movie_dict(movie_id):
    page_json = json.loads(scrape_index_page(movie_id))
    movie = {
        "name": page_json["name"],
        "genre": page_json["genre"],
        "image": page_json["image"],
        "description": page_json["description"],
    }
    print(movie["name"])
    return movie


def get_movies_paged(page=2, movies_per_page=10):
    ids = get_movie_ids(num=movies_per_page, page=page)
    scrape_result = {"movies": []}
    for id in ids:
        scrape_result["movies"].append(collect_movie_dict(id))
    return scrape_result


if __name__ == "__main__":
    ids = get_movie_ids(10)
    print(ids)
    for id in ids:
        collect_movie_dict(id)
