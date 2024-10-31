from modules.dak_api import DakAPI


def execute():
    """実行"""
    api = DakAPI()
    # メタ実験体検索実行
    stats = api.search_meta()
    for character in stats:
        print(f"{character.to_summary()}")
    # バフされた実験体検索実行
    buffed = api.search_buffed()
    for diff in buffed:
        print(f"{diff.to_diff()}")


if __name__ == "__main__":
    execute()
