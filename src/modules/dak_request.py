from typing import List
from modules.stat import Stat
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import csv


class DakRequest(object):
    """Dak.GGから情報を引っ張ってくるクラス"""

    def get_current_patch_stats(self) -> List[Stat]:
        """今パッチのライブ統計取得

        Returns:
            List[Stat]: 今パッチのライブ統計データ
        """
        print("Getting current live stats.")
        url = "https://dak.gg/er/statistics?period=currentPatch&hl=ja"
        live_stats = self.__get_table_from_dakgg(url)
        stats = self.__deserialize_stats(live_stats)
        return stats

    def get_prev_patch_stats(self) -> List[Stat]:
        """前パッチのライブ統計取得

        Returns:
            List[Stat]: 前パッチのライブ統計データ
        """
        print("Getting previous live stats.")
        url = "https://dak.gg/er/statistics?period=prevPatch&hl=ja"
        live_stats = self.__get_table_from_dakgg(url)
        stats = self.__deserialize_stats(live_stats)
        return stats

    def __write_stats_to_csv(self, url: str, header: List[str], stats: List[Stat]) -> None:
        """データをcsvに書き出す
            NOTE: あんまり使わないのでprivateにしてある

        Args:
            url (str): 情報取得対象のURL
            header (List[str]): ヘッダ
            stats (List[Stat]): 統計一覧
        """
        live_stats = self.__get_table_from_dakgg(url)
        header = self.__create_header(live_stats)
        stats = self.__deserialize_stats(live_stats)
        print("Writing stats to csv.")
        with open("./stats.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            for stat in stats:
                stats_row = stat.to_list()
                print(stats_row)
                writer.writerow(stats_row)
        print("Writing completed.")

    def __get_table_from_dakgg(self, url: str) -> pd.DataFrame:
        """データをDakGGから取得する

        Returns:
            pd.DataFrame: 取得したデータ
        """
        # ライブ統計テーブル取得
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options)
        driver.get(url)
        html = driver.page_source
        tables = pd.read_html(html)
        if len(tables) > 1:
            print("Warning : Found multiple tables.")
        # 解析
        live_stats = tables[0]
        return live_stats

    def __create_header(self, live_stats: pd.DataFrame) -> List[str]:
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

    def __deserialize_stats(self, live_stats: pd.DataFrame) -> List[Stat]:
        """こういうのはdeserializeというらしいと聞いた気がするがあっているのだろうか

        Args:
            live_stats (pd.DataFrame): データ

        Returns:
            List[Stat]: 変換後のデータ
        """
        rows = live_stats.values
        stats: List[Stat] = []
        for row in rows:
            # 勝率が"-"の場合をケア
            if row[4] == "-":
                row[4] = "0.0%"
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
