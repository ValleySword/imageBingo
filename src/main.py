#-*- coding:utf-8 -*-

import os
import json
import logging
import argparse
import random

from env.app_parameters import AppParameters
from classes.images_search import ImagesSearch
from classes.parse_condition import parse_json_file
# from classes.gacha import is_ssr
from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import base64

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

def get_args():
    parser = argparse.ArgumentParser(description='Images search')

    parser.add_argument(
        "--isH",
        help="Active H mode",
        default=False,
        action='store_true'
    )

    return parser.parse_args()

# def main():
#     args = get_args()

#     app_parameters = AppParameters()

#     logger = logging.getLogger(name="images_search")
#     logger.setLevel(logging.INFO)

#     logger.info("start : images_search")

#     images_search = imagesSearch(
#         api_key=app_parameters.api_key,
#         custom_search_engine=app_parameters.custom_search_engine,
#         # webhook=app_parameters.discord_webhook,
#         search_max_index=app_parameters.search_max_index,
#         # isH= args.isH and is_ssr(),
#         logger=logger
#     )

#     with open(os.path.join(os.path.dirname(__file__), app_parameters.file_name),encoding='utf-8') as f:
#         file = json.load(f)
#         images_search.execute(parse_json_file(file))

#     logger.info("finished : images_search")
    
@app.route("/")
def index():
    return 'Index Page'

#  ランダムで返すAPI
@app.route("/api/image/random", methods=['GET'])
def get_image_random():
    images_path = "./image"
    images = []
    for i in range(10):
        images.append(random.choice(os.listdir(images_path)))
    json_str = json.dumps(images, ensure_ascii=False)
    return json_str

# 画像名がドメインに入力されてる場合、画像を返すAPI
@app.route('/image', methods=['GET'])
# /image?img=画像名 で画像を表示
def get_image_file():
    # images_path = "./image"
    # パスに注意
    images_path = "./local_images"
    img = request.args.get('img')
    fpath = images_path + "/" + img
    return send_file(fpath)

# 画像すべてをjson形式で返すAPI
@app.route('/prefix', methods=['GET'])
def get_prefix() :
    images_path = "./image"
    images = []
    prefix = request.args.get('prefix')
    if not prefix:
        for img in os.listdir(images_path):
            images.append(img)
    else:
        for img in os.listdir(images_path):
            if img.startswith(prefix):
                images.append(img)

    json_str = json.dumps(images, ensure_ascii=False)
    return json_str
    
@app.route('/search', methods=['GET'])
def search_image() :
    app_parameters = AppParameters()
    images_search = ImagesSearch(
        api_key=app_parameters.api_key,
        custom_search_engine=app_parameters.custom_search_engine,
        search_max_index=app_parameters.search_max_index,
    )
    with open(os.path.join(os.path.dirname(__file__), app_parameters.file_name),mode='rb') as f:
        file = json.load(f)
        # file = f.read()
        return base64.b64encode(images_search.execute(parse_json_file(file)))
        # test = base64.b64encode(test)
    # prefix = request.args.get('prefix')
    # images_path = "./local_images"
    # images = []
    # if not prefix:
    #     for img in os.listdir(images_path):
    #         images.append(img)
    # else:
    #     for img in os.listdir(images_path):
    #         if img.startswith(prefix):
    #             images.append(img)
    # json_str = json.dumps(images, ensure_ascii=False)

    
    return base64.b64encode(images_search.execute(parse_json_file(file)))

@app.route('/keyword', methods=["GET"])
def keyword_change() :
    json_file = open('search.json',encoding="utf-8", mode='r')
    json_data = json.load(json_file)
    json_data[0]["keywords"] = "test"  # 書き換えるワード
    return json.dumps(json_data, ensure_ascii=False)

@app.route("/change", methods=["GET"])
def change() :
    with open("search.json", encoding="utf-8") as f:
        data = json.load(f)
        data[0]["keywords"] = request.args.get("text")
    with open("search.json", encoding="utf-8", mode="w") as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=2))

    app_parameters = AppParameters()
    images_search = ImagesSearch(
        api_key=app_parameters.api_key,
        custom_search_engine=app_parameters.custom_search_engine,
        search_max_index=app_parameters.search_max_index,
    )
    with open(os.path.join(os.path.dirname(__file__), app_parameters.file_name),mode='rb') as f:
        file = json.load(f)
        return base64.b64encode(images_search.execute(parse_json_file(file)))
    
@app.route('/キャベツ', methods=["GET"])
def keyword_cabbage() :
    json_file = open('search.json',encoding="utf-8", mode='r')
    data = json.load(json_file)
    data[0]["keywords"] = "キャベツ"  # 書き換えるワード
    with open("search.json", encoding="utf-8", mode="w") as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=2))
    
    app_parameters = AppParameters()
    images_search = ImagesSearch(
        api_key=app_parameters.api_key,
        custom_search_engine=app_parameters.custom_search_engine,
        search_max_index=app_parameters.search_max_index,
    )
    with open(os.path.join(os.path.dirname(__file__), app_parameters.file_name),mode='rb') as f:
        file = json.load(f)
        return base64.b64encode(images_search.execute(parse_json_file(file)))

@app.route('/レタス', methods=["GET"])
def keyword_lettuce() :
    json_file = open('search.json',encoding="utf-8", mode='r')
    data = json.load(json_file)
    data[0]["keywords"] = "レタス"  # 書き換えるワード
    with open("search.json", encoding="utf-8", mode="w") as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=2))

    app_parameters = AppParameters()
    images_search = ImagesSearch(
        api_key=app_parameters.api_key,
        custom_search_engine=app_parameters.custom_search_engine,
        search_max_index=app_parameters.search_max_index,
    )
    with open(os.path.join(os.path.dirname(__file__), app_parameters.file_name),mode='rb') as f:
        file = json.load(f)
        return base64.b64encode(images_search.execute(parse_json_file(file)))

@app.route('/test', methods=["GET"])
def test() :
    print("testOK")
    app_parameters = AppParameters()
    images_search = ImagesSearch(
        api_key=app_parameters.api_key,
        custom_search_engine=app_parameters.custom_search_engine,
        search_max_index=app_parameters.search_max_index,
    )
    with open(os.path.join(os.path.dirname(__file__), app_parameters.file_name),mode='rb') as f:
        file = json.load(f)
        return base64.b64encode(images_search.execute(parse_json_file(file)))
    



# （失敗）画像すべてをjson形式で返すAPI　!!!パスとして返していた
# @app.route('/test', methods=['GET'])
# def test_image() :
#     images_path = "./image"
#     # iamge = os.listdir(images_path)
#     json_str = json.dumps(os.listdir(images_path), ensure_ascii=False)
#     fpath = images_path + "/" + json_str
#     # return send_file(fpath)
#     return fpath


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5173')


# main()
# サーバ落とすたびに実行されるので一回停止