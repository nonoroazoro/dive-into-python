from sklearn.cluster import KMeans
from sklearn.metrics import calinski_harabaz_score

from .movie_feature import load_encodings


def clustering(p_clusters=5):
    encodings, X = load_encodings()
    labels = KMeans(n_clusters=p_clusters, random_state=8).fit_predict(X)
    score = round(calinski_harabaz_score(X, labels), 2)

    clusters = [{"movies": []} for _ in range(p_clusters)]
    for index, label in enumerate(labels):
        movie = encodings[index]
        clusters[label]["movies"].append(movie["id"])

    return {"clusters": clusters, "labels": labels, "score": score}
