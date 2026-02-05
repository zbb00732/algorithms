"""Python直訳版

    変更点:
     Pythonのfor文はCのように記述するのが困難なので改変している
     Cの配列とPythonのリストの違いによる改変がある
     Cのscanf関数とPythonのinput関数の違いによる改変がある
"""
N = 7

def linsearch(x: int, v: list, n: int):
    p = 0
    while (p < n):
        if (v[p] == x):
            break

        p += 1;

    if (p < n):
        return p
    else:
        return -1

def main():
    a = [0] * N
    for i in range(N):
        a[i] = int(input())

    t = int(input())
    print(linsearch(t, a, N))

if __name__ == '__main__':
    main()
