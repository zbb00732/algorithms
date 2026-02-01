"""Python翻訳版
"""

def inprod(vx: list[float], vy: list[float]) -> float:
    """n次元のベクトルの内積を求める

    Args:
        vx (list[float]): 1つ目のベクトルのリスト（リスト数が次元数）
        vy (list[float]): 2つ目のベクトルのリスト

    Returns:
        float: ベクトルの内積
    """
    # 結果が取得できれば良いのでジェネレータ式で遅延処理
    return sum(x * y for x, y in zip(vx, vy))

def main() -> None:
    # 複数の実数値をCUIより取得
    args = list(map(float, input().split()))

    # x1, y1, x2, y2, ... として受け取るので
    # それをxとyのリストに分割
    vx: list[float] = args[::2]
    vy: list[float] = args[1::2]

    print(inprod(vx, vy))

if __name__ == '__main__':
    main()

