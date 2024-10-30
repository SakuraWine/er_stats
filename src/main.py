from modules.dakgg_api import DakGGAPI
from typing import Optional, List, Tuple
from modules.stat import Stat
import argparse


def extract_character_by_threshold(pick_threshold: Optional[float], win_threshold: Optional[float]) -> List[Stat]:
    api = DakGGAPI()
    stats = api.get_stats()
    if pick_threshold:
        print(f"Pick % threshold : {pick_threshold}%")
        stats = [stat for stat in stats if stat.pick_percentage >= pick_threshold]
    if win_threshold:
        print(f"Win % threshold : {win_threshold}%")
        stats = [stat for stat in stats if stat.win_percentage >= win_threshold]
    return stats


def sort_by_descending_win_percentage(stats: List[Stat]) -> List[Stat]:
    stats.sort(key=lambda stat: stat.win_percentage, reverse=True)
    return stats


def parse_arg() -> Tuple[Optional[float], Optional[float]]:
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pick_threshold")
    parser.add_argument("-w", "--win_threshold")
    args = parser.parse_args()
    pick_threshold = args.pick_threshold
    if pick_threshold:
        pick_threshold = float(pick_threshold)
    win_threshold = args.win_threshold
    if win_threshold:
        win_threshold = float(win_threshold)
    return pick_threshold, win_threshold


def execute():
    pick_threshold, win_threshold = parse_arg()
    stats = extract_character_by_threshold(pick_threshold, win_threshold)
    print("Descending order of Win %.")
    stats.sort(key=lambda stat: stat.win_percentage, reverse=True)
    rank_count = 1
    for character in stats:
        row = f"{rank_count}. " + character.extract()
        print(row)
        rank_count += 1


if __name__ == "__main__":
    execute()
