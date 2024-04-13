<template>
  <div class="rules">
    <h1>ビンゴを見極めるゲーム</h1>
    <p>
      ある2種類の検索ワード（犬、猫など）で調べた画像がビンゴのマスを押すとランダムで出てくる!<br />
      同じワードだと思う画像がタテ、ヨコ、ナナメそろったと思ったらビンゴボタンを押そう！<br />
      ただし、ビンゴになったことに気づかずにボタンを押したら失敗！<br />
      ビンゴになったらすぐにボタンを押そう！<br />
      <strong
        >画像はgoogleで調べたワードで出てきた画像なので必ずしも正しいとは限らない!</strong
      >
    </p>
    <div class="start">
      <p class="mode">モード選択</p>
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
  </div>
</template>

<style>
.rules {
  margin: 80px;
}
p {
  font-size: 24px;
}
.mode {
  margin: 24px;
}
.start {
  margin: 40px;
  font-size: 40px;
}
</style>
