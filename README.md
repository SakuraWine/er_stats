# 概要

DakGGのライブ統計から情報を取得して色々する。

## main.py

ひとまずピック率と勝率の閾値をそれぞれ設定して、閾値を超える実験体の一覧を勝率降順で並べて出力する機能を実装してみた。
他の機能は考え中。

実行例
```bash
$ python main.py --pick_threshold 2.0 --win_threshold 10.0
Getting live stats.
Pick % threshold : 2.0%
Win % threshold : 10.0%
Descending order of Win %.
1. 実験体: アルカナ ユミン, RP: 10.3, Pick: 3.04%, Win: 15.35%, TOP 3: 41.4%, Avg.Rank: 4.3
2. 実験体: 両手剣 雪, RP: 10.9, Pick: 2.37%, Win: 14.13%, TOP 3: 43.02%, Avg.Rank: 4.2
3. 実験体: 突撃小銃 ヘイズ, RP: 6.2, Pick: 2.61%, Win: 14.02%, TOP 3: 39.6%, Avg.Rank: 4.3
4. 実験体: 斧 マーカス, RP: 9.4, Pick: 2.3%, Win: 13.89%, TOP 3: 40.11%, Avg.Rank: 4.3
5. 実験体: 突撃小銃 アヤ, RP: 8.3, Pick: 2.56%, Win: 13.39%, TOP 3: 39.08%, Avg.Rank: 4.3
6. 実験体: 斧 アビゲイル, RP: 6.6, Pick: 2.65%, Win: 12.67%, TOP 3: 36.82%, Avg.Rank: 4.4
7. 実験体: 弓 莉央, RP: 3.8, Pick: 2.57%, Win: 12.15%, TOP 3: 36.17%, Avg.Rank: 4.5
8. 実験体: 狙撃銃 カティア, RP: 3.5, Pick: 2.16%, Win: 12.0%, TOP 3: 36.24%, Avg.Rank: 4.5
9. 実験体: バット ルク, RP: 6.4, Pick: 2.22%, Win: 11.82%, TOP 3: 36.72%, Avg.Rank: 4.5
10. 実験体: 両手剣 デビー&マーリン, RP: 4.8, Pick: 3.31%, Win: 11.74%, TOP 3: 37.8%, Avg.Rank: 4.4
11. 実験体: 金槌 マグヌス, RP: 6.4, Pick: 2.21%, Win: 11.71%, TOP 3: 39.0%, Avg.Rank: 4.3
```

## modules

特に書くことない
