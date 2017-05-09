from .data import pre_process, clustering

if __name__ == "__main__":
    # pre_process()
    results = {}
    for k in range(5, 31, 5):
        results[k] = clustering(k)
    print("good")
