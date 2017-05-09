import numpy as np

from functools import lru_cache
from sklearn.cluster import KMeans
from sklearn.metrics import calinski_harabaz_score

from ..utils import load_csv


def clustering(p_clusters=5):
    X, encodings = __getEncodings()
    labels = KMeans(n_clusters=p_clusters, random_state=8).fit_predict(X)
    score = round(calinski_harabaz_score(X, labels), 2)
    return (labels, score)


@lru_cache()
def __getEncodings():
    encodings = load_csv("encodings")
    X = np.array([list(item["encoding"]) for item in encodings], dtype=np.int)
    return (X, encodings)
