from dataclasses import dataclass
from typing import List


@dataclass
class Stat(object):
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