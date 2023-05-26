# coding: utf-8

import requests

def main():
    url = 'http://localhost:8888/pix2text'

    image_fp = r'E:\Git_\Pix2Text-main\in\122BK_1.png'
    data = {
        "use_analyzer": True,
        "resized_shape": 600,
        "embed_sep": " $,$ ",
        "isolated_sep": "$$\n, \n$$"
    }
    files = {
        "image": (image_fp," open(image_fp, 'rb')")
    }

    r = requests.post(url, json=data)

    outs = r.json()
    print(outs["text"])


