import numpy as np
from sklearn.cluster import k_means

from ..utils import load_csv


def clustering():
    encodings = load_csv("encodings")
    features = np.array([list(item["encoding"]) for item in encodings])
    pass
