# 概要

DakGGのライブ統計から情報を取得して色々する。

## 準備

`pandas`の`read_html`使ってる。
`selenium`の準備も必要。

## Usage

ひとまずピック率と勝率の閾値をそれぞれ設定して、閾値を超える実験体の一覧を勝率降順で並べて出力する機能を実装してみた。
他の機能は考え中。

実行例
```bash
$ python ./src/main.py --pick_threshold 2.0 --win_threshold 10.0
Getting live stats.
Pick % threshold : 2.0%
Win % threshold : 10.0%
Descending order of Win %.
1. 【アルカナ ユミン】 [RP: 10.2] [Pick: 3.07%] [Win: 15.29%] [TOP 3: 41.33%] [Avg.Rank: 4.3]
2. 【両手剣 雪】 [RP: 10.8] [Pick: 2.37%] [Win: 14.11%] [TOP 3: 42.9%] [Avg.Rank: 4.2]
3. 【突撃小銃 ヘイズ】 [RP: 6.1] [Pick: 2.61%] [Win: 14.01%] [TOP 3: 39.5%] [Avg.Rank: 4.3]
4. 【斧 マーカス】 [RP: 9.3] [Pick: 2.31%] [Win: 13.86%] [TOP 3: 40.04%] [Avg.Rank: 4.3]
5. 【突撃小銃 アヤ】 [RP: 8.3] [Pick: 2.57%] [Win: 13.39%] [TOP 3: 39.11%] [Avg.Rank: 4.3]
6. 【斧 アビゲイル】 [RP: 6.6] [Pick: 2.65%] [Win: 12.65%] [TOP 3: 36.78%] [Avg.Rank: 4.4]
7. 【弓 莉央】 [RP: 3.8] [Pick: 2.58%] [Win: 12.18%] [TOP 3: 36.14%] [Avg.Rank: 4.5]
8. 【狙撃銃 カティア】 [RP: 3.5] [Pick: 2.15%] [Win: 12.05%] [TOP 3: 36.27%] [Avg.Rank: 4.5]
9. 【バット ルク】 [RP: 6.5] [Pick: 2.22%] [Win: 11.85%] [TOP 3: 36.69%] [Avg.Rank: 4.5]
10. 【両手剣 デビー&マーリン】 [RP: 4.9] [Pick: 3.31%] [Win: 11.77%] [TOP 3: 37.78%] [Avg.Rank: 4.4]
11. 【金槌 マグヌス】 [RP: 6.4] [Pick: 2.21%] [Win: 11.66%] [TOP 3: 39.15%] [Avg.Rank: 4.3]
```
