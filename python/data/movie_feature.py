import numpy as np
from functools import lru_cache

from ..utils import load_json, load_csv, save_csv


def extract_features(movies):
    casts = set()
    countries = set()
    genres = set()
    tags = set()

    for movie in movies:
        countries.update(movie.get("countries", []))
        genres.update(movie.get("genres", []))
        tags.update(movie.get("tags", []))

        for cast in movie.get("casts", []):
            if "name" in cast:
                casts.add(cast["name"])

    features = set()
    features.update(casts, countries, genres, tags)
    return list(features)


def save_features(features, filename="features"):
    rows = [[feature] for feature in features]
    save_csv(filename, rows)


@lru_cache()
def load_features(filename="features"):
    return [row[0] for row in load_csv(filename, False)]


def encode_features(features, movies):
    encodings = []
    length = len(features)
    for movie in movies:
        encoding = [0] * length
        __encode_feature(movie.get("countries", []), features, encoding)
        __encode_feature(movie.get("genres", []), features, encoding)
        __encode_feature(movie.get("tags", []), features, encoding)
        __encode_feature([cast.get("name") for cast in movie.get("casts", [])], features, encoding)
        encodings.append({
            "id": movie.get("id"),
            "title": movie.get("title"),
            "encoding": "".join(map(str, encoding))
        })

    return encodings


def save_encodings(encodings, filename="encodings"):
    save_csv(filename, encodings, ["id", "title", "encoding"])


@lru_cache()
def load_encodings(filename="encodings"):
    encodings = load_csv(filename)
    X = np.array([list(item["encoding"]) for item in encodings], dtype=np.int)
    return (encodings, X)


def __encode_feature(items, features, encoding):
    for item in items:
        try:
            index = features.index(item)
            encoding[index] = 1
        except ValueError:
            print("{} is not found in features.".format(item))