import numpy as np
from functools import lru_cache
from sklearn.cluster import KMeans
from sklearn.metrics import calinski_harabaz_score

from .movie_feature import load_encodings, load_features, decode_features


def clustering(p_clusters=5):
    encodings, X = load_encodings()
    labels = KMeans(n_clusters=p_clusters, random_state=8).fit_predict(X)
    score = round(calinski_harabaz_score(X, labels), 2)

    clusters = [{"movies": [], "features": []} for _ in range(p_clusters)]
    for index, label in enumerate(labels):
        clusters[label]["movies"].append(encodings[index])

    features = __load_features()
    for cluster in clusters:
        featuresCount = np.zeros((len(features)), dtype=np.int)
        for movie in cluster["movies"]:
            featuresCount += movie["encoding"]
        indexes = np.argsort(-featuresCount)

        # top 5 features
        cluster["features"].extend(features[indexes[:5]])
    return {"clusters": clusters, "labels": labels, "score": score}


@lru_cache()
def __load_features():
    return np.array(load_features())
