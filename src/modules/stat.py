from dataclasses import dataclass
from typing import List


@dataclass
class Stat(object):
    """Statsのような気もするがStatで
    """
    character: str
    rp: float
    pick_percentage: float
    pick_num: int
    win_percentage: float
    top3_percentage: float
    average_rank: float
    average_damages: float
    average_tks: float
    average_player_kills: float
    average_animal_kills: float

    def to_list(self) -> List[str]:
        """文字列リストに変換

        Returns:
            List[str]: 文字列リスト
        """
        return [
            self.character,
            str(self.rp),
            str(self.pick_percentage),
            str(self.pick_num),
            str(self.win_percentage),
            str(self.top3_percentage),
            str(self.average_rank),
            str(self.average_damages),
            str(self.average_tks),
            str(self.average_player_kills),
            str(self.average_animal_kills),
        ]

    def extract(self) -> str:
        """いい感じの出力情報に変換する

        Returns:
            str: いい感じの文字列
        """
        return f"実験体: {self.character}, RP: {self.rp}, Pick: {self.pick_percentage}%, Win: {self.win_percentage}%, TOP 3: {self.top3_percentage}%, Avg.Rank: {self.average_rank}"
