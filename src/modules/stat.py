from dataclasses import dataclass
from typing import List, Dict


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

    def __sub__(self, other: "Stat") -> "Stat":
        """2つの統計情報の差を求める

        Args:
            other (Stat): 比較対象の統計情報

        Returns:
            Stat: 差
        """
        if self.character != other.character:
            raise ValueError(f"False comparison [{self.character} and {other.character}]")
        rp = self.rp - other.rp
        pick_percentage = self.pick_percentage - other.pick_percentage
        pick_num = self.pick_num - other.pick_num
        win_percentage = self.win_percentage - other.win_percentage
        top3_percentage = self.top3_percentage - other.top3_percentage
        average_rank = self.average_rank - other.average_rank
        average_damages = self.average_damages - other.average_damages
        average_tks = self.average_tks - other.average_tks
        average_player_kills = self.average_player_kills - other.average_player_kills
        average_animal_kills = self.average_animal_kills - other.average_animal_kills
        return Stat(
            self.character,
            round(rp, 2),
            round(pick_percentage, 2),
            round(pick_num, 2),
            round(win_percentage, 2),
            round(top3_percentage, 2),
            round(average_rank, 2),
            round(average_damages, 2),
            round(average_tks, 2),
            round(average_player_kills, 2),
            round(average_animal_kills, 2),
        )

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

    def to_summary(self) -> str:
        """いい感じの出力情報に変換する

        Returns:
            str: いい感じの文字列
        """
        return f"【{self.character}】 [RP: {self.rp}] [Pick: {self.pick_percentage}%] [Win: {self.win_percentage}%] [TOP 3: {self.top3_percentage}%] [Avg.Rank: {self.average_rank}]"

    def to_diff(self) -> str:
        """差分として出力する際の情報に変換する

        Returns:
            str: いい感じの文字列
        """
        rp = "+" + str(self.rp) if self.rp > 0 else str(self.rp)
        pick_percentage = "+" + str(self.pick_percentage) if self.pick_percentage > 0 else str(self.pick_percentage)
        # pick_num = "+" + str(self.pick_num) if self.pick_num > 0 else str(self.pick_num)
        win_percentage = "+" + str(self.win_percentage) if self.win_percentage > 0 else str(self.win_percentage)
        top3_percentage = "+" + str(self.top3_percentage) if self.top3_percentage > 0 else str(self.top3_percentage)
        average_rank = "+" + str(self.average_rank) if self.average_rank > 0 else str(self.average_rank)
        # average_damages = "+" + str(self.average_damages) if self.average_damages > 0 else str(self.average_damages)
        # average_tks = "+" + str(self.average_tks) if self.average_tks > 0 else str(self.average_tks)
        # average_player_kills = "+" + str(self.average_player_kills) if self.average_player_kills > 0 else str(self.average_player_kills)
        # average_animal_kills = "+" + str(self.average_animal_kills) if self.average_animal_kills > 0 else str(self.average_animal_kills)
        return f"【{self.character}】 [RP: {rp}] [Pick: {pick_percentage}%] [Win: {win_percentage}%] [TOP 3: {top3_percentage}%] [Avg.Rank: {average_rank}]"
