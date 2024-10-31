# 概要

DakGGのライブ統計から情報を取得して色々する。

## 準備

`pandas`の`read_html`使ってる。
`selenium`の準備も必要。

## Usage

メタキャラっぽい実験体と強くなったっぽい実験体をそれぞれ出力する。
メタキャラと判定する条件は、ピック率が2%かつ勝率が13%以上
強くなったと判定する条件は、前回パッチと今回パッチの統計を比較して、ピック率が下がっておらず、勝率が0.5%より大きく上昇していること。

実行例
```bash
$ python ./src/main.py
Searching meta character.
Getting current live stats.
Pick % threshold : 2.0%
Win % threshold : 13.0%
Descending order of Win %.
【突撃小銃 ヘイズ】 [RP: 6.9] [Pick: 2.57%] [Win: 14.24%] [TOP 3: 39.39%] [Avg.Rank: 4.3]
【両手剣 雪】 [RP: 10.6] [Pick: 2.3%] [Win: 14.05%] [TOP 3: 42.69%] [Avg.Rank: 4.2]
【斧 マーカス】 [RP: 9.9] [Pick: 2.1%] [Win: 14.0%] [TOP 3: 40.49%] [Avg.Rank: 4.3]
【突撃小銃 アヤ】 [RP: 8.7] [Pick: 2.39%] [Win: 13.29%] [TOP 3: 39.42%] [Avg.Rank: 4.3]
Searching buffed character.
Getting current live stats.
Getting previous live stats.
Error : Character not found : アルカナ ユミン
New character may implemented in current patch.
【斧 マーカス】 [RP: +0.7] [Pick: +0.41%] [Win: +0.89%] [TOP 3: +1.15%] [Avg.Rank: 0.0]
【レイピア エレナ】 [RP: +0.3] [Pick: +0.01%] [Win: +0.84%] [TOP 3: +0.34%] [Avg.Rank: -0.1]
【双剣 カミロ】 [RP: +0.5] [Pick: +0.09%] [Win: +0.73%] [TOP 3: +0.62%] [Avg.Rank: -0.1]
【グローブ ヒョヌ】 [RP: -1.1] [Pick: +0.11%] [Win: +0.53%] [TOP 3: -0.47%] [Avg.Rank: 0.0]
【鞭 マイ】 [RP: -0.8] [Pick: +0.04%] [Win: +0.56%] [TOP 3: +0.07%] [Avg.Rank: 0.0]
【バット スア】 [RP: +1.7] [Pick: +0.08%] [Win: +1.14%] [TOP 3: +2.15%] [Avg.Rank: 0.0]
【アルカナ シャーロット】 [RP: +1.7] [Pick: +0.16%] [Win: +2.38%] [TOP 3: +0.58%] [Avg.Rank: 0.0]
【アルカナ ヨハン】 [RP: +2.4] [Pick: +0.17%] [Win: +0.81%] [TOP 3: +2.37%] [Avg.Rank: -0.1]
【斧 ジャッキー】 [RP: +0.9] [Pick: +0.05%] [Win: +0.61%] [TOP 3: +0.85%] [Avg.Rank: -0.1]
【レイピア フィオラ】 [RP: +1.1] [Pick: +0.04%] [Win: +2.36%] [TOP 3: +0.02%] [Avg.Rank: -0.1]
```
