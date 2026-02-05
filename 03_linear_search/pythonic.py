"""Python翻訳版
"""

N = 7

def linsearch(x: int, v: list[int], n: int) -> int:
    """1次元の表の線形探索

    Args:
        x (int): 探索する値
        v (list[int]): 1次元の表
        n (int): 

    Returns:
        int: マッチしたらその値のインデックス、アンマッチなら-1
    """

    # 表の長さ分のループ
    for i in range(n):
        # 探索する値とマッチしたら値を返す
        if v[i] == x:
            return i
    # アンマッチなら-1を返す
    return -1

def main():
    """エントリポイント
    """
    
    # 入力を全て受け取りリストにする
    l = list(map(int, input().split()))

    # 1番目からN番目までの値をスライスで切り出す
    a = l[:N]

    # N+1番目の値を取り出す
    t = l[N]

    # 線形探索を行い、結果を表示する
    print(linsearch(t, a, N))

if __name__ == '__main__':
    main()

