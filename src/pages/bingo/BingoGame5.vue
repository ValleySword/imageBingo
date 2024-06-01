<template>
  <v-btn class="bingo-btn" @click="bingoCheck()">ビンゴ！</v-btn>
  <div class="answer">
    <h2 v-if="ans == 'out'">ビンゴになったのに気づかなかった！不正解！</h2>
    <h2 v-if="ans == true">正解！</h2>
    <h2 v-if="ans == false">不正解...</h2>
    <div>
      <v-btn v-if="imgDisp" @click="reload()" class="reload"
        >もう一度プレイ</v-btn
      >
      <router-link to="/bingoRule" v-if="imgDisp">戻る</router-link>
    </div>
  </div>
  <div class="squares">
    <div v-for="imgData in imgDatas" :key="imgData.id">
      <span
        v-if="imgDisp && imgData.name && !(imgData.id == 13)"
        :class="{
          'imgs-name-hover': hoverFlag && !(imgData.id == 13),
          'imgs-name': !hoverFlag,
        }"
      >
        {{ imgData.name }}
      </span>
      <img
        v-if="!(imgData.src == '')"
        :src="imgData.src"
        :class="{
          imgs: !imgDisp || hoverFlag || imgData.id == 13,
          'imgs-clear': imgDisp && !hoverFlag && !(imgData.id == 13),
        }"
        @mouseover="hoverOn"
        @mouseleave="hoverOff"
      />
      <v-btn
        v-if="imgData.src == ''"
        @click="randomImg2(imgData)"
        width="200px"
        height="200px"
        >押してね</v-btn
      >
    </div>
  </div>
  <!-- <div class="full-image-wrap" v-if="fullImage">
    <v-btn v-if="fullImage" @click="close">閉じる</v-btn>
    <img class="full-image" :src="fullImageSrc" />
  </div> -->
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      modeWord: '',
      wordList: [],
      // load: '',
      imgDatas: [
        { id: 1, name: '', src: '' }, // id:ID, name:検索ワード, src:画像,
        { id: 2, name: '', src: '' },
        { id: 3, name: '', src: '' },
        { id: 4, name: '', src: '' },
        { id: 5, name: '', src: '' },
        { id: 6, name: '', src: '' },
        { id: 7, name: '', src: '' },
        { id: 8, name: '', src: '' },
        { id: 9, name: '', src: '' },
        { id: 10, name: '', src: '' },
        { id: 11, name: '', src: '' },
        { id: 12, name: '', src: '' },
        { id: 13, name: 'free', src: 'src/local_images/free_icon.png' },
        { id: 14, name: '', src: '' },
        { id: 15, name: '', src: '' },
        { id: 16, name: '', src: '' },
        { id: 17, name: '', src: '' },
        { id: 18, name: '', src: '' },
        { id: 19, name: '', src: '' },
        { id: 20, name: '', src: '' },
        { id: 21, name: '', src: '' },
        { id: 22, name: '', src: '' },
        { id: 23, name: '', src: '' },
        { id: 24, name: '', src: '' },
        { id: 25, name: '', src: '' },
      ],
      fullImageSrc: '',
      fullImage: null,
      checker: false,
      imgDisp: false,
      ans: null,
      btnChecker: false,
      hoverFlag: false,
    };
  },
  mounted() {
    this.modeWord = this.$route.query.value;
    console.log(this.modeWord);
    this.wordChange();
    console.log(this.wordList);
  },
  computed: {
    computedImgDatas() {
      return JSON.parse(JSON.stringify(this.imgDatas));
    },
  },
  watch: {
    computedImgDatas: {
      handler: function (newImgs, oldImgs) {
        let changeId = 0;
        for (const newImg of newImgs) {
          if (newImg.name !== oldImgs[newImg.id - 1].name) {
            console.log(newImg.id);
            changeId = newImg;
            break; // 不要なループ省略のため
          }
        }
        if (this.bingoRoot(changeId)) {
          if (this.checker) {
            console.log('ビンゴ過ぎた');
            return (this.checker = 'out');
          }
          this.checker = true;
          console.log('今ビンゴ');
        }
      },
      deep: true,
    },
  },
  methods: {
    hoverOn() {
      if (!this.imgDisp) {
        return;
      }
      this.hoverFlag = true;
    },
    hoverOff() {
      if (!this.imgDisp) {
        return;
      }
      this.hoverFlag = false;
    },
    randomImg2(imgData) {
      let randomNum = Math.floor(Math.random() * 100);
      if (randomNum == 0) {
        randomNum += 1;
      }
      if (Math.random() < 0.5) {
        imgData.name = this.wordList[0];
        // console.log(imgData.name); 答え
        imgData.src = `src/local_images/${this.wordList[0]}${randomNum}.jpg`;
      } else {
        imgData.name = this.wordList[1];
        // console.log(imgData.name); 答え
        imgData.src = `src/local_images/${this.wordList[1]}${randomNum}.jpg`;
      }
    },
    wordChange() {
      if (this.modeWord == 'cabbage') {
        this.wordList = ['キャベツ', 'レタス'];
      } else if (this.modeWord == 'dog') {
        this.wordList = ['犬', '猫'];
      } else if (this.modeWord == 'bridge') {
        this.wordList = ['はし', '橋'];
      }
    },
    randomImg(num) {
      const randomNum = Math.floor(Math.random() * 100);
      if (randomNum == 0) {
        randomNum += 1;
      }
      if (Math.random() < 0.5) {
        this.imgDatas[num].name = this.wordList[0];
        console.log(this.imgDatas[num].name);
        // console.log(randomNum);
        this.imgDatas[num].src =
          `src/local_images/${this.wordList[0]}${randomNum}.jpg`;
      } else {
        this.imgDatas[num].name = this.wordList[1];
        console.log(this.imgDatas[num].name);
        // console.log(randomNum);
        this.imgDatas[num].src =
          `src/local_images/${this.wordList[1]}${randomNum}.jpg`;
      }
    },
    bingoRoot(changeImg) {
      const i = this.imgDatas;
      let word = '';
      // ワード判定
      if (changeImg.name == this.wordList[0]) {
        word = this.wordList[0];
      } else {
        word = this.wordList[1];
      }
      if (
        (i[0].name == word &&
          i[6].name == word &&
          i[18].name == word &&
          i[24].name == word) ||
        (i[4].name == word &&
          i[8].name == word &&
          i[16].name == word &&
          i[20].name == word) ||
        (i[2].name == word &&
          i[7].name == word &&
          i[17].name == word &&
          i[22].name == word) ||
        (i[10].name == word &&
          i[11].name == word &&
          i[13].name == word &&
          i[14].name == word) ||
        (i[0].name == word &&
          i[1].name == word &&
          i[2].name == word &&
          i[3].name == word &&
          i[4].name == word) ||
        (i[5].name == word &&
          i[6].name == word &&
          i[7].name == word &&
          i[8].name == word &&
          i[9].name == word) ||
        (i[15].name == word &&
          i[16].name == word &&
          i[17].name == word &&
          i[18].name == word &&
          i[19].name == word) ||
        (i[20].name == word &&
          i[21].name == word &&
          i[22].name == word &&
          i[23].name == word &&
          i[24].name == word) ||
        (i[0].name == word &&
          i[5].name == word &&
          i[10].name == word &&
          i[15].name == word &&
          i[20].name == word) ||
        (i[1].name == word &&
          i[6].name == word &&
          i[11].name == word &&
          i[16].name == word &&
          i[21].name == word) ||
        (i[2].name == word &&
          i[7].name == word &&
          i[17].name == word &&
          i[22].name == word) ||
        (i[3].name == word &&
          i[8].name == word &&
          i[13].name == word &&
          i[18].name == word &&
          i[23].name == word) ||
        (i[4].name == word &&
          i[9].name == word &&
          i[14].name == word &&
          i[19].name == word &&
          i[24].name == word)
      ) {
        return true;
      }
      return false;
    },
    imageClick(i) {
      this.fullImageSrc = this.imgDatas[i].src;
      this.fullImage = true;
    },
    close() {
      this.fullImage = false;
    },
    bingoCheck() {
      if (this.btnChecker) {
        return;
      }
      this.imgDisp = true;
      if (this.checker == 'out') {
        this.ans = 'out';
      } else if (this.checker) {
        console.log('BINGO');
        this.ans = true;
      } else {
        console.log('NOBINGO');
        this.ans = false;
      }
      this.btnChecker = true;
    },
    reload() {
      location.reload();
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

<style scoped>
.bingo-btn {
  margin: 40px;
  width: 200px;
}
.answer {
  margin: 40px;
  font-size: 32px;
}
.imgs {
  position: relative;
  width: 200px;
  height: 200px;
  overflow: hidden;
}
.imgs-clear {
  position: relative;
  width: 200px;
  height: 200px;
  overflow: hidden;
  opacity: 0.3;
}
.imgs-name {
  position: absolute;
  font-size: 24px;
  z-index: 1;
  color: rgb(100, 0, 255);
}
.imgs-name-hover {
  position: absolute;
}
.back {
  margin: 32px;
  font-size: 24px;
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
.left-btn {
  display: grid;
  grid-template-columns: 240px;
}
.center-btn {
  display: grid;
  grid-template-columns: 0 240px;
}
.right-btn {
  display: grid;
  grid-template-columns: 0 0 240px;
}
.squares {
  display: grid;
  justify-content: center;
  grid-template-rows: 200px 200px 200px 200px 200px;
  grid-template-columns: 200px 200px 200px 200px 200px;
}
.loading {
  padding: 40px;
}
.reload {
  margin-right: 24px;
}
.left-ans {
  /* writing-mode: vertical-rl; 右から左に縦書き 横にしたかったが、なぜか下段が文字曲がるため出来ない */
  position: absolute; /* 相対位置指定 */
  left: 360px;
}
.center-ans {
  position: absolute;
  left: 740px;
  top: 360px;
}
.right-ans {
  position: absolute;
  right: 360px;
}
.btm-ans {
  position: absolute;
  top: 1120px;
  left: 748px;
}
.tes {
  width: 240px;
  height: 240px;
}
</style>
