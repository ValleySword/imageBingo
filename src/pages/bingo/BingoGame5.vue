<template>
  <h2 class="title">BINGOゲーム（仮）</h2>
  <div class="full-image-wrap" v-if="fullImage">
    <v-btn v-if="fullImage" @click="close">閉じる</v-btn>
    <img class="full-image" :src="fullImageSrc" />
  </div>
  <div class="squares">
    <div>
      <img :src="imgDatas[0].src" width="240px" @click="imageClick(0)" />
      <v-btn v-if="this.imgDatas[0].src == ''" @click="randomImg(0)"
        >レタスかも</v-btn
      >
    </div>
    <div>
      <img :src="imgDatas[1].src" width="240px" @click="imageClick(1)" />
      <v-btn v-if="this.imgDatas[1].src == ''" @click="randomImg(1)"
        >キャベツかも</v-btn
      >
    </div>
    <div>
      <img :src="imgDatas[2].src" width="240px" @click="imageClick(2)" />
      <v-btn v-if="this.imgDatas[2].src == ''" @click="randomImg(2)"
        >レタスかも</v-btn
      >
    </div>
    <div>
      <img :src="imgDatas[3].src" width="240px" @click="imageClick(3)" />
      <v-btn v-if="this.imgDatas[3].src == ''" @click="randomImg(3)"
        >キャベツかも</v-btn
      >
    </div>
    <div>
      <img :src="imgDatas[4].src" width="240px" @click="imageClick(4)" />
      <v-btn v-if="this.imgDatas[4].src == ''" @click="randomImg(4)"
        >レタスかも</v-btn
      >
    </div>
    <div>
      <img :src="imgDatas[5].src" width="240px" @click="imageClick(5)" />
      <v-btn v-if="this.imgDatas[5].src == ''" @click="randomImg(5)"
        >キャベツかも</v-btn
      >
    </div>
    <div>
      <img :src="imgDatas[6].src" width="240px" @click="imageClick(6)" />
      <v-btn v-if="this.imgDatas[6].src == ''" @click="randomImg(6)"
        >レタスかも</v-btn
      >
    </div>
    <div>
      <img :src="imgDatas[7].src" width="240px" @click="imageClick(7)" />
      <v-btn v-if="this.imgDatas[7].src == ''" @click="randomImg(7)"
        >キャベツかも</v-btn
      >
    </div>
    <div>
      <img :src="imgDatas[8].src" width="240px" @click="imageClick(8)" />
      <v-btn v-if="this.imgDatas[8].src == ''" @click="randomImg(8)"
        >レタスかも</v-btn
      >
    </div>
    <div>
      <img :src="imgDatas[9].src" width="240px" @click="imageClick(9)" />
      <v-btn v-if="this.imgDatas[9].src == ''" @click="randomImg(9)"
        >キャベツかも</v-btn
      >
    </div>
    <div>
      <img :src="imgDatas[10].src" width="240px" @click="imageClick(10)" />
      <v-btn v-if="this.imgDatas[10].src == ''" @click="randomImg(10)"
        >レタスかも</v-btn
      >
    </div>
    <div>
      <img :src="imgDatas[11].src" width="240px" @click="imageClick(11)" />
      <v-btn v-if="this.imgDatas[11].src == ''" @click="randomImg(11)"
        >キャベツかも</v-btn
      >
    </div>
    <div>
      <img src="../../local_images/free_icon.png" width="240px" />
    </div>
    <div>
      <img :src="imgDatas[12].src" width="240px" @click="imageClick(12)" />
      <v-btn v-if="this.imgDatas[12].src == ''" @click="randomImg(12)"
        >レタスかも</v-btn
      >
    </div>
    <div>
      <img :src="imgDatas[13].src" width="240px" @click="imageClick(13)" />
      <v-btn v-if="this.imgDatas[13].src == ''" @click="randomImg(13)"
        >キャベツかも</v-btn
      >
    </div>
    <div>
      <img :src="imgDatas[14].src" width="240px" @click="imageClick(14)" />
      <v-btn v-if="this.imgDatas[14].src == ''" @click="randomImg(14)"
        >レタスかも</v-btn
      >
    </div>
    <div>
      <img :src="imgDatas[15].src" width="240px" @click="imageClick(15)" />
      <v-btn v-if="this.imgDatas[15].src == ''" @click="randomImg(15)"
        >キャベツかも</v-btn
      >
    </div>
    <div>
      <img :src="imgDatas[16].src" width="240px" @click="imageClick(16)" />
      <v-btn v-if="this.imgDatas[16].src == ''" @click="randomImg(16)"
        >レタスかも</v-btn
      >
    </div>
    <div>
      <img :src="imgDatas[17].src" width="240px" @click="imageClick(17)" />
      <v-btn v-if="this.imgDatas[17].src == ''" @click="randomImg(17)"
        >キャベツかも</v-btn
      >
    </div>
    <div>
      <img :src="imgDatas[18].src" width="240px" @click="imageClick(18)" />
      <v-btn v-if="this.imgDatas[18].src == ''" @click="randomImg(18)"
        >レタスかも</v-btn
      >
    </div>
    <div>
      <img :src="imgDatas[19].src" width="240px" @click="imageClick(19)" />
      <v-btn v-if="this.imgDatas[19].src == ''" @click="randomImg(19)"
        >キャベツかも</v-btn
      >
    </div>
    <div>
      <img :src="imgDatas[20].src" width="240px" @click="imageClick(20)" />
      <v-btn v-if="this.imgDatas[20].src == ''" @click="randomImg(20)"
        >レタスかも</v-btn
      >
    </div>
    <div>
      <img :src="imgDatas[21].src" width="240px" @click="imageClick(21)" />
      <v-btn v-if="this.imgDatas[21].src == ''" @click="randomImg(21)"
        >キャベツかも</v-btn
      >
    </div>
    <div>
      <img :src="imgDatas[22].src" width="240px" @click="imageClick(22)" />
      <v-btn v-if="this.imgDatas[22].src == ''" @click="randomImg(22)"
        >レタスかも</v-btn
      >
    </div>
    <div>
      <img :src="imgDatas[23].src" width="240px" @click="imageClick(23)" />
      <v-btn v-if="this.imgDatas[23].src == ''" @click="randomImg(23)"
        >キャベツかも</v-btn
      >
    </div>
  </div>
  <!-- <p class="loading">{{ load }}</p> -->
  <!-- <img
    :src="imgData.src"
    v-for="imgData in imgDatas"
    :key="imgData.id"
    width="300px"
    /> -->
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      load: '',
      imgDatas: [
        { name: '', number: 0, src: '' }, // name:検索ワード, number:配置識別番号, src:画像,
        { name: '', number: 1, src: '' },
        { name: '', number: 2, src: '' },
        { name: '', number: 3, src: '' },
        { name: '', number: 4, src: '' },
        { name: '', number: 5, src: '' },
        { name: '', number: 6, src: '' },
        { name: '', number: 7, src: '' },
        { name: '', number: 8, src: '' },
        { name: '', number: 9, src: '' },
        { name: '', number: 10, src: '' },
        { name: '', number: 11, src: '' },
        { name: '', number: 12, src: '' },
        { name: '', number: 13, src: '' },
        { name: '', number: 14, src: '' },
        { name: '', number: 15, src: '' },
        { name: '', number: 16, src: '' },
        { name: '', number: 17, src: '' },
        { name: '', number: 18, src: '' },
        { name: '', number: 19, src: '' },
        { name: '', number: 20, src: '' },
        { name: '', number: 21, src: '' },
        { name: '', number: 22, src: '' },
        { name: '', number: 23, src: '' },
      ],
      fullImageSrc: '',
      fullImage: null,
    };
  },
  methods: {
    randomImg(num) {
      const randomNum = Math.floor(Math.random() * 100);
      if (Math.random() < 0.5) {
        this.imgDatas[num].name = 'キャベツ';
        console.log(this.imgDatas[num].name);
        console.log(randomNum);
        this.imgDatas[num].src =
          `src/local_images/キャベツ${randomNum}.jpg`;
      } else {
        this.imgDatas[num].name = 'レタス';
        console.log(this.imgDatas[num].name);
        console.log(randomNum);
        this.imgDatas[num].src = `src/local_images/レタス${randomNum}.jpg`;
      }
    },
    imageClick(i) {
      this.fullImageSrc = this.imgDatas[i].src;
      this.fullImage = true;
    },
    close() {
      this.fullImage = false;
    },
    async searchBtn(number) {
      // 未使用関数
      this.load = '読み込み中';
      if (number % 2 == 0) {
        console.log('キャベツ');
        this.imgDatas[number].name = 'キャベツ';
        console.log(this.imgDatas[number].name);
      } else {
        console.log('レタス');
        this.imgDatas[number].name = 'レタス';
      }
      await axios
        .get(`http://127.0.0.1:5173/${this.imgDatas[number].name}`)
        .then((response) => {
          this.imgDatas[number].src =
            `data:image/png;base64,${response.data}`;
          this.load = '';
        })
        .catch((error) => {
          this.load = '';
          console.log('error');
          console.log(error);
          this.load = '画像読み込み失敗。もう一度検索してね';
        });
    },
    async lettuceBtn(number) {
      // 未使用
      this.load = '読み込み中';
      await axios
        .get('http://127.0.0.1:5173/lettuce')
        .then((response) => {
          this.imgDatas[number].src =
            `data:image/png;base64,${response.data}`;
          this.load = '';
        })
        .catch((error) => {
          this.load = '';
          console.log('error');
          console.log(error);
          this.load = '画像読み込み失敗。もう一度押してね';
        });
    },
  },
};
</script>

<style>
.title {
  padding: 80px;
}
.full-image {
  width: 600px;
  height: auto;
  display: block;

  position: fixed;
  top: 100px;
  left: 50%;
  transform: translate(-50%);
}
.full-image-wrap {
  background-color: rgba(0, 0, 0, 0.8);
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
}
.squares {
  display: grid;
  justify-content: center;
  grid-template-rows: 240px 240px 240px 240px 240px;
  grid-template-columns: 240px 240px 240px 240px 240px;
}
.loading {
  padding: 40px;
}
</style>
