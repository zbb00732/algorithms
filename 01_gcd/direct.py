"""Python直訳版

変更点:
    Pythonには変数宣言のみの文はないのでNoneを代入している

"""

def gcd(m: int, n: int):
    r, t = None, None
    if m < n:
        t = m
        m = n
        n = t

    while n != 0:
        r = m % n
        m = n
        n = r

    return m

x, y = map(int, input().split())
print(gcd(x, y))

