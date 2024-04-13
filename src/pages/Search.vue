<template>
  <!-- <v-btn @click="changeWord()">json書き込みtest</v-btn> -->
  <!-- <v-btn @click="keyWord()">json読み込みtest</v-btn> -->
  <div class="title">
    <h2>ただの画像検索（1日100回まで）</h2>
  </div>
  <v-row
    style="display: flex; justify-content: center; align-items: center"
  >
    <v-col cols="5">
      <v-col>
        <v-text-field
          v-model="searchWord"
          label="検索キーワード"
        ></v-text-field>
      </v-col>
      <v-btn @click="imagesSearch()">画像検索</v-btn>
    </v-col>
  </v-row>
  <div class="load">
    <h3>{{ load }}</h3>
  </div>
  <v-row>
    <v-col v-for="imgData in imgDatas" :key="imgData.id" cols="4">
      <img :src="imgData.src" width="300px" />
      <v-btn @click="imgDelete(imgData)">削除</v-btn>
    </v-col>
  </v-row>
  <!-- テストが何に使うのか忘れてしまった。確認して削除 -->
  <!-- <v-btn @click="test()">テスト</v-btn> -->
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      searchWord: '',
      load: '',
      imgDatas: [],
    };
  },
  methods: {
    // async test() {
    //   await axios
    //     .get('http://127.0.0.1:5173/キャベツ')
    //     .then((response) => {
    //       console.log(response);
    //     });
    // },
    async imagesSearch() {
      if (!this.searchWord) {
        return (this.load = '検索ワードを入れてね');
      }
      this.load = '読み込み中';
      await axios
        .get(`http://127.0.0.1:5173/change?text=${this.searchWord}`)
        .then(async (response) => {
          // console.log('data:image/png;base64,' + response.data);
          await this.imgDatas.push({
            name: this.searchWord,
            src: `data:image/png;base64,${response.data}`,
          });
          // console.log(this.imgDatas);

          // for (const img of response.data) {
          //   await this.imgDatas.push({
          //     name: img,
          //     src: `http://127.0.0.1:5173/image?img=${img}`,
          //   });
          // }
          // for (const img of response.data) {
          //   console.log(img);
          //   // const imgTag = document.createElement("img")
          //   // imgTag.src = `http://127.0.0.1:5173/image?img=${img}`
          //   await this.imgDatas.push({
          //     name: img,
          //     src: `http://127.0.0.1:5173/image?img=${img}`,
          //   });
          // }
          this.load = '';
        })
        .catch((error) => {
          this.load = '';
          console.log('error');
          console.log(error);
          this.load = '画像読み込み失敗。もう一度検索してね';
        });
    },
    async keyWord() {
      await axios
        .get('http://127.0.0.1:5173/keyword')
        .then(async (response) => {
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async changeWord() {
      this.load = 'キーワード変更中';
      console.log(this.searchWord);
      await axios
        .get(`http://127.0.0.1:5173/change?text=${this.searchWord}`)
        .then(async (response) => {
          console.log('data:image/png;base64,' + response.data);
          await this.imgDatas.push({
            name: 'test',
            src: `data:image/png;base64,${response.data}`,
          });
          console.log(this.imgDatas);
        })
        .catch((error) => {
          console.log(error);
        });
      this.load = '';
    },
    imgDelete(img) {
      this.imgDatas = this.imgDatas.filter((data) => data !== img);
    },
  },
};
</script>

<style>
.title {
  margin: 24px;
}
.load {
  margin: 24px;
}
</style>

<!-- <template> 一度無効に
  <div>
    <v-col cols="12">
      <v-btn @click="imagesSearch()">画像検索</v-btn>
    </v-col>
    <p>{{ load }}</p>
    <v-col cols="auto">
      <v-col cols="1">
        <img
          :src="imgData.src"
          v-for="imgData in imgDatas"
          :key="imgData.id"
          height="150px"
          width="150px"
        />
      </v-col>
    </v-col>
  </div>
</template>
<script>
import axios from 'axios';

export default {
  data() {
    return {
      load: '',
      imgDatas: [],
    };
  },
  methods: {
    async imagesSearch() {
      this.load = '読み込み中';
      await axios
        .get('http://127.0.0.1:5173/search')
        .then(async (response) => {
          this.errorCode = '';
          console.log(
            'data:image/png;base64,' + response.data
          );
          await this.imgDatas.push({
            name: 'test',
            src: `data:image/png;base64,${response.data}`,
          });
          console.log(this.imgDatas);
          // for (const img of response.data) {
          //   await this.imgDatas.push({
          //     name: img,
          //     src: `http://127.0.0.1:5173/image?img=${img}`,
          //   });
          // }
          // for (const img of response.data) {
          //   console.log(img);
          //   // const imgTag = document.createElement("img")
          //   // imgTag.src = `http://127.0.0.1:5173/image?img=${img}`
          //   await this.imgDatas.push({
          //     name: img,
          //     src: `http://127.0.0.1:5173/image?img=${img}`,
          //   });
          // }
          this.load = '';
        })
        .catch((error) => {
          this.load = '';
          console.log('error');
          console.log(error);
          this.load =
            '画像読み込み失敗。もう一度検索してね';
        });
    },
  },
};
</script> -->
