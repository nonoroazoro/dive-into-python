from ..utils import load_json, save_csv, load_csv


def prepare():
    raw_data = load_json("raw_movies")
    features = extract_features(raw_data)
    save_features(features)

    features = load_csv("features")
    return raw_data


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
    return features


def save_features(features):
    rows = [[feature] for feature in features]
    save_csv("features", rows=rows)
