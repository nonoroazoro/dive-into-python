from .movie_feature import extract_features, save_features, load_features, encode_features, save_encodings

from ..utils import load_json


def pre_process():
    __extract_features()
    __encoding_features()


def __extract_features():
    """extract features of movies to file."""

    movies = load_json("raw_movies")
    features = extract_features(movies)
    save_features(features)


def __encoding_features():
    """encoding features to file."""

    features = load_features()
    movies = load_json("raw_movies")
    encodings = encode_features(features, movies)
    save_encodings(encodings)
