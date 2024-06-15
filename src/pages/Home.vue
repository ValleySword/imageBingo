<template>
  <div id="home">
    <div class="header">
      <!-- <img
        src="../local_images/free_icon.png"
        alt="アプリのロゴ"
        class="logo"
      /> -->
      <p>タイトル</p>
      <h1 class="titles">{{ titles[titleNum] }}</h1>
    </div>
    <!-- <div class="navbar"> いつか作りたい
      <button @click="openSettings">設定</button>
      <button @click="openHelp">ヘルプ</button>
      <button @click="openProfile">プロフィール</button>
    </div> -->
    <div class="app-selection">
      <h2>アプリを選択してください</h2>
      <div class="apps">
        <div class="app">
          <router-link to="/search" class="router">
            <img src="../local_images/search.png" alt="画像検索" />
            <h3>画像検索</h3>
          </router-link>
          <p>Googleから画像を検索しよう！</p>
        </div>
        <div class="app">
          <router-link to="/bingoRule" class="router">
            <img src="../local_images/bingo-card.png" alt="ビンゴゲーム" />
            <h3>ビンゴゲーム</h3>
          </router-link>
          <p>画像を使ってビンゴを完成させよう！</p>
        </div>
        <div class="app">
          <img src="../local_images/ai_talk_ai.png" alt="その他のアプリ" />
          <h3 class="others">その他のアプリ</h3>
          <p>今後追加予定のアプリはこちら</p>
        </div>
      </div>
    </div>
    <!-- <div class="future-apps">
      <h2>今後追加予定のアプリ</h2>
      <div class="apps">
        <div class="app">
          <img alt="アプリ1" />
          <p>アプリ1</p>
        </div>
        <div class="app">
          <img alt="アプリ2" />
          <p>アプリ2</p>
        </div>
        <div class="app">
          <img alt="アプリ3" />
          <p>アプリ3</p>
        </div>
      </div>
    </div> -->
  </div>
</template>

<script>
export default {
  data() {
    return {
      titles: [
        '画像探検隊',
        '写真の楽園',
        'ビジュアルワールド',
        'イメージアドベンチャー',
        'フォトの楽園',
        'ピクセル探検隊',
        '写真の宝庫',
        'ビジュアルプレイグラウンド',
        '画像のワンダーランド',
        'フォトの冒険',
        'イメージパラダイス',
        '写真の楽園',
        'ビジュアルギャラリー',
        '画像の楽園',
        'フォトプレイス',
        'イメージエクスプローラー',
        'ピクチャーワールド',
        '画像マジック',
        'フォトワンダーランド',
        'ビジュアルパーク',
        '画像の冒険',
        'ピクチャーパレット',
        'フォトランド',
        '画像エクスペディション',
        'フォトエクスプローラー',
        'ビジュアルクエスト',
        'イメージファンタジー',
        'フォトアドベンチャー',
        'ビジュアルワンダー',
        'イメージスペース',
      ],
      titleNum: 0,
    };
  },
  mounted() {
    this.randomTitle();
  },
  methods: {
    randomTitle() {
      this.titleNum = Math.floor(Math.random() * (22 - 1));
    },
    openSettings() {
      // 設定画面を開くロジックをここに追加します
      console.log('設定を開く');
    },
    openHelp() {
      // ヘルプ画面を開くロジックをここに追加します
      console.log('ヘルプを開く');
    },
    openProfile() {
      // プロフィール画面を開くロジックをここに追加します
      console.log('プロフィールを開く');
    },
  },
};
</script>

<style>
#home {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}

.header {
  text-align: center;
  margin-bottom: 20px;
}

.logo {
  width: 100px;
  height: auto;
}

.titles {
  font-size: 40px;
}

h2 {
  margin: 24px;
}

.others {
  margin: 16px;
}

.navbar {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.navbar button {
  font-size: 14px;
  padding: 10px;
  cursor: pointer;
  background-color: #008cba;
  color: white;
  border: none;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.navbar button:hover {
  background-color: #007bb5;
}

.app-selection {
  text-align: center;
  margin-bottom: 40px;
  width: 100%; /* 幅を80%に設定 */
}

.app-selection .apps {
  display: flex;
  justify-content: space-around; /* 要素間の間隔を調整 */
  gap: 20px;
}

.app {
  flex: 1; /* 各アプリカードの幅を均等に */
  max-width: 400px; /* 最大幅を設定 */
  text-align: center;
}

.app img {
  width: 300px;
  height: auto;
  border-radius: 10px;
  transition: transform 0.3s;
}

.app:hover img {
  transform: scale(1.1);
}

.app p {
  margin: 10px 0 0;
}

.future-apps {
  text-align: center;
  width: 100%; /* 幅を80%に設定 */
}

.future-apps .apps {
  display: flex;
  justify-content: space-around; /* 要素間の間隔を調整 */
  gap: 20px;
}

.future-apps .app {
  flex: 1; /* 各アプリカードの幅を均等に */
  max-width: 150px; /* 最大幅を設定 */
  text-align: center;
}

.future-apps .app img {
  width: 100%;
  height: auto;
  border-radius: 10px;
}
.router {
  font-size: 32px;
}
</style>
