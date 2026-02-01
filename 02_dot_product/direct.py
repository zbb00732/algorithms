"""Python直訳版

変更点:
    Pythonのfor文はCのように記述するのが困難なので改変している
    Cの配列とPythonのリストの違いによる改変がある
    Cのscanf関数とPythonのinput関数の違いによる改変がある
"""

def inprod(x: list[float], y: list[float], n: int) -> float:
    s = 0.0
    for i in range(n):
        s = s + x[i] * y[i]

    return s

def main() -> None:
    a: list[float] = [0.0] * 3
    b: list[float] = [0.0] * 3
    a[0], b[0], a[1], b[1], a[2], b[2] = map(float, input().split())
    print(inprod(a, b, 3))

if __name__ == '__main__':
    main()

