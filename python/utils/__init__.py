import csv
import json


def save_json(name, data):
    path = "data/out/{}.json".format(name)
    with open(path, mode="w", encoding="utf-8") as fp:
        json.dump(data, fp, ensure_ascii=False)


def load_json(name):
    path = "data/in/{}.json".format(name)
    with open(path, mode="r", encoding="utf-8") as fp:
        return json.load(fp)


def save_csv(name, rows, headers=None):
    path = "data/out/{}.csv".format(name)
    with open(path, mode="w", encoding="utf-8") as fp:
        if rows:
            if headers:
                fw = csv.DictWriter(fp, headers)
                fw.writeheader()
                fw.writerows(rows)
            else:
                fw = csv.writer(fp)
                fw.writerows(rows)


def load_csv(name, include_header=True):
    path = "data/out/{}.csv".format(name)
    with open(path, mode="r", encoding="utf-8") as fp:
        if include_header:
            fr = csv.DictReader(fp)
        else:
            fr = csv.reader(fp)
        return list(fr)
