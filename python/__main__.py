from .data import pre_process, clustering, save_clusters

if __name__ == "__main__":
    # pre_process()
    results = {}
    for k in range(5, 31, 5):
        results[k] = clustering(k)
    save_clusters(results)
    print("good")
