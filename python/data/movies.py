from ..utils import load_json, save_csv, load_csv


def pre_process():
    # load raw data.
    movies = load_json("raw_movies")

    # extract features.
    _save_features(_extract_features(movies))


def encode_features():
    movies = load_json("raw_movies")
    features = [row[0] for row in load_csv("features", False)]
    length = len(features)

    encodings = []
    for movie in movies:
        encoding = [0] * length
        _encode_feature(movie.get("countries", []), features, encoding)
        _encode_feature(movie.get("genres", []), features, encoding)
        _encode_feature(movie.get("tags", []), features, encoding)
        _encode_feature([cast.get("name") for cast in movie.get("casts", [])],
                        features, encoding)
        encodings.append({
            "id": movie.get("id"),
            "title": movie.get("title"),
            "encoding": "".join(map(str, encoding))
        })

    save_csv("encodings", encodings, ["id", "title", "encoding"])
    return encodings


def _encode_feature(items, features, encoding):
    for item in items:
        try:
            index = features.index(item)
            encoding[index] = 1
        except ValueError:
            print("{} is not found in features.".format(item))


def _extract_features(movies):
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


def _save_features(features):
    rows = [[feature] for feature in features]
    save_csv("features", rows)
