<template>
  <div class="whole">
    <h1>ビンゴ（を見極める）ゲーム</h1>
    <p class="heading">ルール説明</p>
    <div class="rules">
      1. ビンゴのようにマスが配置されたボードがあります。<br /><br />
      2.
      各マスを押すとランダムに<strong>Google画像検索から取得された画像</strong>が表示されます。<br />
      <span class="note"
        >※
        マスを押したとき出現する画像は2種類の検索ワード（例：犬と猫）のどちらかが表示されます。<br /><strong
          class="attention"
          >googleが思う画像なので猫が猫とは限らない！</strong
        ></span
      ><br />
      3.
      縦、横、ナナメに同じ検索ワードの画像が揃ったらと思ったらビンゴボタンを押します。<br /><br />
      クリア条件：ビンゴ成立時ビンゴボタンクリックでゲームクリア。<br /><strong
        >成立前にビンゴボタンを押したり、成立後にマスを押すとゲーム失敗です。</strong
      >
      <h2>画面タッチでも出来る！</h2>
    </div>
    <div class="start">
      <p class="mode" style="padding: 16px">モード選択</p>
      <button v-if="!mode" @click="mode = 'mode3'">3×3モード</button>
      <button v-if="!mode" @click="mode = 'mode5'">5×5モード</button>
      <div v-if="mode == 'mode3'">
        <h4>3×3モード</h4>
        <p>初級</p>
        <router-link :to="{ path: '/bingo3', query: { value: 'dog' } }"
          >犬or猫</router-link
        >
        <p>中級</p>
        <router-link :to="{ path: '/bingo3', query: { value: 'cabbage' } }"
          >キャベツorレタス</router-link
        >
        <p>上級</p>
        <router-link :to="{ path: '/bingo3', query: { value: 'bridge' } }"
          >はしor橋</router-link
        >
      </div>
      <div v-if="mode == 'mode5'">
        <p>ビンゴするかも不明！超高難易度！</p>
        <h4>5×5モード</h4>
        <router-link :to="{ path: '/bingo5', query: { value: 'dog' } }"
          >スーパー犬orスーパー猫</router-link
        >
        <br />
        <router-link :to="{ path: '/bingo5', query: { value: 'cabbage' } }"
          >スーパーキャベツorスーパーレタス</router-link
        >
        <br />
        <router-link :to="{ path: '/bingo5', query: { value: 'bridge' } }"
          >スーパーはしorスーパー橋</router-link
        >
      </div>
      <button v-if="mode" @click="mode = ''" class="mode">
        モード選択に戻る
      </button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      mode: '',
    };
  },
};
</script>

<style>
.whole {
  margin: 80px;
}
p {
  font-size: 24px;
}
.attention {
  display: inline-block; /* ブロック化 */
  font-size: 120%; /* 文字を大きくする */
  border-bottom: 2px solid #0059b3; /* 下線 */
  color: #ff1111;
}
.start {
  margin: 40px;
  font-size: 40px;
}
.mode {
  font-size: 24px;
  font-weight: bold;
}
.heading {
  font-size: 32px;
  font-family: Arial;
  color: #3399ff;
  line-height: 3;
}
.rules {
  text-align: left; /* 左揃えにする */
  margin: 0 auto; /* 中央寄りに配置する */
  max-width: 960px; /* ボックスの最大幅を設定する */
  font-size: 24px; /* 文字のサイズを大きくする */
  line-height: 1.6; /* 行間を調整する */
}

.note {
  display: block;
  margin-top: 5px; /* ※ の行に余白を追加 */
}
</style>
