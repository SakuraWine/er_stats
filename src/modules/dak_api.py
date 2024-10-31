from typing import List, Optional
from .dak_request import DakRequest
from modules.stat import Stat


class DakAPI(object):
    """APIという程のものでもないけどAPI"""
    def __init__(self) -> None:
        self.request = DakRequest()

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
        # NOTE: 現在は固定で勝率が高い順にソートしている
        stats.sort(key=lambda stat: stat.win_percentage, reverse=True)
        return stats

    def search_meta(self) -> List[Stat]:
        """環境で強そうな実験体を探す

        Returns:
            List[Stat]: 強そうな実験体の情報一覧
        """
        stats = self.request.get_current_patch_stats()
        # TODO: 強そうな実験体の条件を検討する
        return stats

    def search_buffed(self) -> List[Stat]:
        """前回のパッチから統計が良くなった実験体を探す

        Returns:
            List[Stat]: 強くなっていそうな実験体を探す
        """
        print("Searching BUFFED character.")
        diff_stats: List[Stat] = []
        current_stats = self.request.get_current_patch_stats()
        prev_stats = self.request.get_prev_patch_stats()
        prev_stats = {stat.character: stat for stat in prev_stats}
        for current_stat in current_stats:
            if not current_stat.character in prev_stats:
                print(f"Character not found : {current_stat.character}")
                continue
            prev_stat = prev_stats[current_stat.character]
            diff_stat = current_stat - prev_stat
            diff_stats.append(diff_stat)
        return diff_stats
