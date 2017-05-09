from .data import pre_process, encode_features, clustering

if __name__ == "__main__":
    # pre_process()
    # encode_features()
    results = {}
    for k in range(5, 31, 5):
        results[k] = clustering(k)
    print("good")
