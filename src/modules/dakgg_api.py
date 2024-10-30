from typing import List
from modules.stat import Stat
from selenium import webdriver
import pandas as pd
import csv


class DakGGAPI(object):
    """APIというほどのものでもないけどAPIということで"""
    URL = "https://dak.gg/er/statistics?hl=ja"

    def get_stats(self) -> List[Stat]:
        """各キャラの統計一覧を取得する

        Returns:
            List[Stat]: 統計一覧
        """
        live_stats = self.get_table_from_dakgg()
        stats = self.deserialize_stats(live_stats)
        return stats

    def write_stats_to_csv(self, header: List[str], stats: List[Stat]) -> None:
        """データをcsvに書き出す

        Args:
            header (List[str]): ヘッダ
            stats (List[Stat]): 統計一覧
        """
        live_stats = self.get_table_from_dakgg()
        header = self.create_header(live_stats)
        stats = self.deserialize_stats(live_stats)
        print("Writing stats to csv.")
        with open("./stats.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            for stat in stats:
                stats_row = stat.to_list()
                print(stats_row)
                writer.writerow(stats_row)
        print("Writing completed.")

    def get_table_from_dakgg(self) -> pd.DataFrame:
        """データをDakGGから取得する

        Returns:
            pd.DataFrame: 取得したデータ
        """
        # ライブ統計テーブル取得
        print("Getting live stats.")
        driver = webdriver.Chrome()
        driver.get(self.URL)
        html = driver.page_source
        tables = pd.read_html(html)
        if len(tables) > 1:
            print("Warning : Found multiple tables.")
        # 解析
        live_stats = tables[0]
        return live_stats

    def create_header(self, live_stats: pd.DataFrame) -> List[str]:
        """DakGGから取得したデータからヘッダを作成する

        Args:
            live_stats (pd.DataFrame): データ

        Returns:
            List[str]: ヘッダ
        """
        # ヘッダ取得
        header = list(live_stats.columns)
        # NOTE: ランクを削除し、ピック%とピック数を別のセルに記録するためにヘッダの整形が必要
        header = header[1:4] + ["#Pick"] + header[4:]
        return header

    def deserialize_stats(self, live_stats: pd.DataFrame) -> List[Stat]:
        """こういうのはdeserializeというらしいと聞いた気がするがあっているのだろうか

        Args:
            live_stats (pd.DataFrame): データ

        Returns:
            List[Stat]: 変換後のデータ
        """
        rows = live_stats.values
        stats: List[Stat] = []
        for row in rows:
            pick_data = row[3].split("%")
            stat = Stat(
                character=row[1],
                rp=float(row[2]),
                pick_percentage=float(pick_data[0]),
                pick_num=int(pick_data[1]),
                win_percentage=float(row[4].replace("%", "")),
                top3_percentage=float(row[5].replace("%", "")),
                average_rank=float(row[6].replace("#", "")),
                average_damages=float(row[7]),
                average_tks=float(row[8]),
                average_player_kills=float(row[9]),
                average_animal_kills=float(row[10]),
            )
            stats.append(stat)
        return stats
