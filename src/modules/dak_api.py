from typing import List, Optional
from dakgg.src.modules.dak_request import DakRequest
from modules.stat import Stat


class DakAPI(object):
    """APIという程のものでもないけどAPI"""
    def get_stats(self) -> List[Stat]:
        """ライブ統計取得

        Returns:
            List[Stat]: ライブ統計データ
        """
        request = DakRequest()
        return request.get_stats()

    def search_by_threshold(self, pick_threshold: Optional[float], win_threshold: Optional[float]) -> List[Stat]:
        """条件に合致するデータを取得して勝率が高い順に並べ替える

        Args:
            pick_threshold (Optional[float]): ピック率の閾値
            win_threshold (Optional[float]): 勝率の閾値

        Returns:
            List[Stat]: 勝率降順のデータ
        """
        stats = self.get_stats()
        if pick_threshold:
            print(f"Pick % threshold : {pick_threshold}%")
            stats = [stat for stat in stats if stat.pick_percentage >= pick_threshold]
        if win_threshold:
            print(f"Win % threshold : {win_threshold}%")
            stats = [stat for stat in stats if stat.win_percentage >= win_threshold]
        # NOTE: 現在は固定で勝率が高い順にソートしている
        stats.sort(key=lambda stat: stat.win_percentage, reverse=True)
        return stats
