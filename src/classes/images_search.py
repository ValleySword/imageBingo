import random

# from .discord_sender import DiscordSender
from .google_image import GoogleImage
from .interfaces.images_search_condition import ImagesSearchCondition

import requests
import json
import os
import shutil
# import cv2
# import base64


class ImagesSearch:
    def __init__(
        self,
        api_key,
        custom_search_engine,
        # webhook,
        search_max_index,
        # logger,
        # *,
        # isH
    ):
        # self.discord_sender = DiscordSender(webhook, logger)
        self.google_image = GoogleImage(api_key, custom_search_engine)
        self.search_max_index = search_max_index
        # self.logger = logger
        # self.isH = isH

    def decide_condition(self, search_conditions):
        return random.choice(search_conditions)

    def execute(self, search_conditions):
        target:ImagesSearchCondition = self.decide_condition(search_conditions)

        start_index:int = random.randint(1, self.search_max_index)

        # キーワードがまったく同じであっても結果がまったく同じになるというわけではない
        keyword = target.keywords
        # print(keyword) ちゃんと検索ワードが渡されているか確認

        link_list = self.google_image.get_link_list(
            f"{keyword}" if "" else keyword,
            start_index
        )
        # 画像を一枚に絞るための処理？
        link = random.choice(link_list)
        image = self.google_image.get_image(link)

        # 画像1枚（ローカル保存処理をする場合はコメントアウト）
        return image

        # jImage = cv2.imencode(".jpg", image)
        # img = cv2.imread(image)
        # img_str = str(img)
        # img_byte = base64.b64encode(img_str).decode("utf-8")
        # img_json = json.dumps({'image': img_byte}).encode('utf-8')

        # if link_list:
        # text = f"{target.name} : {target.success}"
        # print(self.google_image.get_image(link_list))


        # get_image は画像1枚ずつ
        # for i in link_list :
        #     print(self.google_image.get_image(i))
        # print("images_searchaaaaaaaaaaaaaaaaaaaaaa")
        # return self.google_image.get_image(link)
    
    # ローカル保存処理（ローカルに保存しない場合はコメントアウト）
        # for i in link_list:
        #     with open('count.json', 'r') as file:
        #         count = json.load(file)
        #         count['count'] += 1
        #     with open('count.json', 'w') as f:
        #         json.dump(count, f)
        #         print(count['count'])
        #     with open(f"./local_images/{keyword}{count['count']}.jpg", 'wb') as file:
        #         file.write(self.google_image.get_image(i))

            # returnで処理が終了？するので1枚しか保存できない（そのためローカル保存する場合はコメントアウト）
            # return self.google_image.get_image(link)
        # else:
        #     text = f"{target.name} : {target.error}"
        #     print(text)

