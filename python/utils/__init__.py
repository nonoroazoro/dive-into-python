import csv
import json


def load_json(name):
    path = "data/in/{}.json".format(name)
    with open(path, mode="r", encoding="utf-8") as fp:
        return json.load(fp)


def save_json(name, data):
    path = "data/out/{}.json".format(name)
    with open(path, mode="w", encoding="utf-8") as fp:
        json.dump(data, fp, ensure_ascii=False)


def load_csv(name):
    path = "data/out/{}.csv".format(name)
    with open(path, mode="r", encoding="utf-8") as fp:
        fr = csv.reader(fp)
        return tuple(fr)


def save_csv(name, headers=None, rows=None):
    path = "data/out/{}.csv".format(name)
    with open(path, mode="w", encoding="utf-8") as fp:
        fw = csv.writer(fp)
        if headers:
            fw.writerow(headers)
        if rows:
            fw.writerows(rows)
