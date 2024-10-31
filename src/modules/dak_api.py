from typing import List, Optional
from .dak_request import DakRequest
from modules.stat import Stat


class DakAPI(object):
    # 強くなったと判断するピック率と勝率の閾値。前回パッチと今回パッチでの値の差が以下を上回っていたら強くなったと判断する
    # TODO: 適当に決めているので検討が必要かもしれない
    BUFFED_PICK_THRESHOLD = 0.0
    BUFFED_WIN_THRESHOLD = 0.5

    # 環境で強そうと判断するピック率と勝率の閾値。今回パッチでの統計が以下の値を上回っていたら強そうと判断する
    # TODO: これも適当に決めている
    META_PICK_THRESHOLD = 2.0
    META_WIN_THRESHOLD = 13.0

    """APIという程のものでもないけどAPI"""
    def __init__(self) -> None:
        self.request = DakRequest()

    def search_meta(self) -> List[Stat]:
        """環境で強そうな実験体を探す

        Returns:
            List[Stat]: 強そうな実験体の情報一覧
        """
        print("Searching meta character.")
        print(f"Pick % threshold : {self.META_PICK_THRESHOLD}%")
        print(f"Win % threshold : {self.META_WIN_THRESHOLD}%")
        stats = self.search_by_threshold(pick_threshold=self.META_PICK_THRESHOLD, win_threshold=self.META_WIN_THRESHOLD)
        if len(stats) == 0:
            print("Meta character not found...")
        else:
            # 勝率降順に並び替える
            print("Descending order of Win %.")
            stats.sort(key=lambda stat: stat.win_percentage, reverse=True)
        return stats

    def search_buffed(self) -> List[Stat]:
        """前回のパッチから統計が良くなった実験体を探す

        Returns:
            List[Stat]: 強くなっていそうな実験体を探す
        """
        print("Searching buffed character.")
        diff_stats = self.get_diff_prev_and_current()
        stats = [stat for stat in diff_stats if stat.pick_percentage > self.BUFFED_PICK_THRESHOLD and stat.win_percentage > self.BUFFED_WIN_THRESHOLD]
        if len(stats) == 0:
            print("Buffed character not found...")
        return stats

    def search_by_threshold(self, pick_threshold: Optional[float], win_threshold: Optional[float]) -> List[Stat]:
        """条件に合致するデータを取得して勝率が高い順に並べ替える

        Args:
            pick_threshold (Optional[float]): ピック率の閾値
            win_threshold (Optional[float]): 勝率の閾値

        Returns:
            List[Stat]: 勝率降順のデータ
        """
        stats = self.request.get_current_patch_stats()
        if pick_threshold:
            print(f"Pick % threshold : {pick_threshold}%")
            stats = [stat for stat in stats if stat.pick_percentage >= pick_threshold]
        if win_threshold:
            print(f"Win % threshold : {win_threshold}%")
            stats = [stat for stat in stats if stat.win_percentage >= win_threshold]
        return stats

    def get_diff_prev_and_current(self) -> List[Stat]:
        """各実験帯の前回パッチと今回パッチの差を取得する

        Returns:
            List[Stat]: 差一覧
        """
        diff_stats: List[Stat] = []
        current_stats = self.request.get_current_patch_stats()
        prev_stats = self.request.get_prev_patch_stats()
        prev_stats = {stat.character: stat for stat in prev_stats}
        for current_stat in current_stats:
            if not current_stat.character in prev_stats:
                print(f"Error : Character not found : {current_stat.character}")
                print("New character may implemented in current patch.")
                continue
            prev_stat = prev_stats[current_stat.character]
            diff_stat = current_stat - prev_stat
            diff_stats.append(diff_stat)
        return diff_stats
