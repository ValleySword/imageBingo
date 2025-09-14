# ビンゴ当てゲーム

マスを押すと2種類の画像が表示されます。

その種類がタテヨコナナメそろったと思ったらビンゴボタンを押して確認。

揃っていたら成功、もしそろっていなかったら失敗。

キャベツとレタスなど、揃っているかどうか見分けづらいものもあるので注意！

# 画像検索機能

googleの画像検索API（Google Custom Search API）を利用して、画像を検索可能

APIの使用回数制限があるため、1日100回のみ利用可能

# デモ

### ビンゴ当てゲーム

<img width="1519" height="935" alt="スクリーンショット 2025-09-14 104411" src="https://github.com/user-attachments/assets/fcc0bef3-fd94-4160-aea3-c00f9b6bd805" />


### 画像検索機能

<img width="1519" height="936" alt="スクリーンショット 2025-09-14 104102" src="https://github.com/user-attachments/assets/31a41635-88f5-49a7-8a66-3ddf0abd82bd" />


# 使用方法

リポジトリのクローン、インストール、起動

```bash
git clone git@github.com:ValleySword/imageBingo.git
cd imageBingo
npm install # 初回のみ
npm run dev
# 2025年9月追記：npm run dev実行後、エラーが出ます。
# 問題なく動作するので、無視して大丈夫です。
# 現在エラーの原因を調査中です。
```

画像検索機能の実行方法

```bash
# ターミナルをもう一つ開く
# envフォルダのenv.exampleをコピーして、envフォルダの中に.envファイルを作成
cd src
python main.py
```

# コミットの仕方

忘れてしまわないように、コミット方法を一応記載

1. git add .
2. git commit -m "メッセージ"
3. git push origin main

# その他

作成時期：2023年12月
