"""Python翻訳版
"""

def gcd(m: int, n: int) -> int:
    """ユークリッドの互除法で最大公約数を求める

    Args:
        m (int): 自然数
        n (int): 自然数

    Returns:
        int: 最大公約数
    """

    # m > n でなければ m と n を入れ替える
    if m < n:
        m, n = n, m

    # 単純なループで処理可能なので
    # 再帰処理ではなくループ処理を選択
    while n != 0:
        m, n = n, m % n

    return m

def main():
    """エントリポイント
    """

    # 入力を受け取る
    m, n = map(int, input().split())

    # 最大公約数を表示
    print(gcd(m, n))

if __name__ == '__main__':
    main()

