<template>
  <v-btn class="bingo-btn" @click="bingoCheck()">ビンゴ！</v-btn>
  <!-- <v-btn>ビンゴにならなかった！</v-btn> -->
  <div class="answer">
    <h2 v-if="ans == 'out'">ビンゴになったのに気づかなかった！不正解！</h2>
    <h2 v-if="ans == true">正解！</h2>
    <h2 v-if="ans == false">不正解...</h2>
  </div>
  <div class="squares">
    <div v-for="imgData in imgDatas" :key="imgData.id">
      <p
        v-if="imgDisp && imgData.name && !(imgData.id == 5)"
        :class="com(imgData.id)"
      >
        {{ imgData.name }}
      </p>
      <img v-if="!(imgData.src == '')" :src="imgData.src" width="240px" />
      <v-btn
        v-if="imgData.src == ''"
        @click="randomImg2(imgData)"
        width="240px"
        height="240px"
        >押してね</v-btn
      >
    </div>
  </div>
  <div class="back">
    <v-btn v-if="imgDisp" @click="reload()" class="reload"
      >もう一度プレイ</v-btn
    >
    <router-link to="/bingoRule" v-if="imgDisp">戻る</router-link>
  </div>
  <div class="full-image-wrap" v-if="fullImage">
    <v-btn v-if="fullImage" @click="close">閉じる</v-btn>
    <img class="full-image" :src="fullImageSrc" />
  </div>
  <!-- <div class="squares">
    <div>
      <p v-if="imgDisp" class="left-ans">{{ this.imgDatas[0].name }}</p>
      <img :src="imgDatas[0].src" width="240px" @click="imageClick(0)" />
      <v-btn
        v-if="this.imgDatas[0].src == ''"
        @click="randomImg(0)"
        width="240px"
        height="240px"
        >押してね</v-btn
      >
    </div>
    <div>
      <p v-if="imgDisp" class="top-ans">{{ this.imgDatas[1].name }}</p>
      <img :src="imgDatas[1].src" width="240px" @click="imageClick(1)" />
      <v-btn
        v-if="this.imgDatas[1].src == ''"
        @click="randomImg(1)"
        width="240px"
        height="240px"
        >押してね</v-btn
      >
    </div>
    <div>
      <p v-if="imgDisp" class="right-ans">{{ this.imgDatas[2].name }}</p>
      <img :src="imgDatas[2].src" width="240px" @click="imageClick(2)" />
      <v-btn
        v-if="this.imgDatas[2].src == ''"
        @click="randomImg(2)"
        width="240px"
        height="240px"
        >押してね</v-btn
      >
    </div>
    <div>
      <p v-if="imgDisp" class="left-ans">{{ this.imgDatas[3].name }}</p>
      <img :src="imgDatas[3].src" width="240px" @click="imageClick(3)" />
      <v-btn
        v-if="this.imgDatas[3].src == ''"
        @click="randomImg(3)"
        width="240px"
        height="240px"
        >押してね</v-btn
      >
    </div>
    <div>
      <img src="../../local_images/free_icon.png" width="240px" />
    </div>
    <div>
      <p v-if="imgDisp" class="right-ans">{{ this.imgDatas[4].name }}</p>
      <img :src="imgDatas[4].src" width="240px" @click="imageClick(4)" />
      <v-btn
        v-if="this.imgDatas[4].src == ''"
        @click="randomImg(4)"
        width="240px"
        height="240px"
        >押してね</v-btn
      >
    </div>
    <div>
      <p v-if="imgDisp" class="left-ans">{{ this.imgDatas[5].name }}</p>
      <img :src="imgDatas[5].src" width="240px" @click="imageClick(5)" />
      <v-btn
        v-if="this.imgDatas[5].src == ''"
        @click="randomImg(5)"
        width="240px"
        height="240px"
        >押してね</v-btn
      >
    </div>
    <div>
      <img :src="imgDatas[6].src" width="240px" @click="imageClick(6)" />
      <v-btn
        v-if="this.imgDatas[6].src == ''"
        @click="randomImg(6)"
        width="240px"
        height="240px"
        >押してね</v-btn
      >
      <p v-if="imgDisp" class="btm-ans">{{ this.imgDatas[6].name }}</p>
    </div>
    <div>
      <p v-if="imgDisp" class="right-ans">{{ this.imgDatas[7].name }}</p>
      <img :src="imgDatas[7].src" width="240px" @click="imageClick(7)" />
      <v-btn
        v-if="this.imgDatas[7].src == ''"
        @click="randomImg(7)"
        width="240px"
        height="240px"
        >押してね</v-btn
      >
    </div>
  </div> -->
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
      modeWord: '',
      wordList: [],
      // load: '',
      imgDatas: [
        { id: 1, name: '', src: '' }, // id:ID, name:検索ワード, src:画像,
        { id: 2, name: '', src: '' },
        { id: 3, name: '', src: '' },
        { id: 4, name: '', src: '' },
        { id: 5, name: 'free', src: 'src/local_images/free_icon.png' },
        { id: 6, name: '', src: '' },
        { id: 7, name: '', src: '' },
        { id: 8, name: '', src: '' },
        { id: 9, name: '', src: '' },
      ],
      fullImageSrc: '',
      fullImage: null,
      checker: false,
      imgDisp: false,
      ans: null,
      btnChecker: false,
    };
  },
  mounted() {
    this.modeWord = this.$route.query.value;
    console.log(this.modeWord);
    this.wordChange();
    console.log(this.wordList);
  },
  watch: {
    imgDatas: {
      handler: function () {
        if (this.bingoRoot()) {
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
    // マス目のv-forに適応してたが、squaresを使ってみたら上手くいった
    com(id) {
      if (id == 1 || id == 4 || id == 7) {
        return 'left-ans';
      }
      if ((id == 2, id == 5)) {
        return 'center-ans';
      }
      if (id == 3 || id == 6 || id == 9) {
        return 'right-ans';
      }
      if (id == 8) {
        return 'btn-ans';
      }
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
      console.log(imgData);
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
    bingoRoot() {
      const i = this.imgDatas;
      const c = this.wordList[0];
      const l = this.wordList[1];
      if (
        (i[0].name == c && i[7].name == c) ||
        (i[2].name == c && i[5].name == c) ||
        (i[3].name == c && i[4].name == c) ||
        (i[1].name == c && i[6].name == c) ||
        (i[0].name == l && i[7].name == l) ||
        (i[2].name == l && i[5].name == l) ||
        (i[3].name == l && i[4].name == l) ||
        (i[1].name == l && i[6].name == l) ||
        (i[0].name == c && i[1].name == c && i[2].name == c) ||
        (i[5].name == c && i[6].name == c && i[7].name == c) ||
        (i[0].name == c && i[3].name == c && i[5].name == c) ||
        (i[2].name == c && i[4].name == c && i[7].name == c) ||
        (i[0].name == l && i[1].name == l && i[2].name == l) ||
        (i[5].name == l && i[6].name == l && i[7].name == l) ||
        (i[0].name == l && i[3].name == l && i[5].name == l) ||
        (i[2].name == l && i[4].name == l && i[7].name == l)
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
.senter-btn {
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
  grid-template-rows: 240px 240px 240px;
  grid-template-columns: 240px 240px 240px;
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
.top-ans {
  position: absolute;
  top: 388px;
  left: 728px;
}
.right-ans {
  position: absolute;
  right: 360px;
}
.btm-ans {
  position: absolute;
  top: 1144px;
  left: 728px;
}
.tes {
  width: 240px;
  height: 240px;
}
</style>
