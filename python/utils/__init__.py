import json


def load_json(p_name):
    path = "data/in/{}.json".format(p_name)
    with open(path, mode="r", encoding="utf-8") as fp:
        return json.load(fp)


def save_json(p_data, p_name):
    path = "data/out/{}.json".format(p_name)
    with open(path, mode="w", encoding="utf-8") as fp:
        json.dump(p_data, fp, ensure_ascii=False)
