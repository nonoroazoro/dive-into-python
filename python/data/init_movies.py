from ..utils import load_json, save_json


def prepare():
    data = load_json("raw_movies")
    extract_tags(data)
    return data


def extract_tags(p_raw_data):
    genres = set()
    people = set()

    # for movie in p_raw_data:
    #     del movie["feature"]

    # save_json(p_raw_data[0], "movie")
