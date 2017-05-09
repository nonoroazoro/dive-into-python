from functools import lru_cache

from ..utils import load_json
from .movie_feature import extract_features, save_features, load_features, encode_features, save_encodings


def pre_process():
    __extract_features()
    __encoding_features()


def __extract_features():
    """extract features of movies to file."""

    movies = __load_movies()
    features = extract_features(movies)
    save_features(features)


def __encoding_features():
    """encoding features to file."""

    movies = __load_movies()
    features = load_features()
    encodings = encode_features(features, movies)
    save_encodings(encodings)


@lru_cache()
def __load_movies():
    return load_json("raw_movies")
