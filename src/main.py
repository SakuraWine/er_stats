from modules.dak_api import DakAPI
from typing import Optional, Tuple
import argparse


def parse_arg() -> Tuple[Optional[float], Optional[float]]:
    """コマンドライン引数解析

    Returns:
        Tuple[Optional[float], Optional[float]]: 解析後の引数
    """
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
    """実行"""
    pick_threshold, win_threshold = parse_arg()
    if not any([pick_threshold, win_threshold]):
        print("No threshold were given.")
        exit(0)
    api = DakAPI()
    stats = api.search_by_threshold(pick_threshold, win_threshold)
    print("Descending order of Win %.")
    stats.sort(key=lambda stat: stat.win_percentage, reverse=True)
    rank_count = 1
    for character in stats:
        row = f"{rank_count}. " + character.to_summary()
        print(row)
        rank_count += 1
    diff = api.search_buffed()
    for character in diff:
        print(f"{character.to_diff()}")
        rank_count += 1


if __name__ == "__main__":
    execute()
