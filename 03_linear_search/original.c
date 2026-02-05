/**
 * 問題:
 *      整数のデータからなる表に対して
 *      与えられたデータがその表の中にあるかどうか探し
 *      あればその位置を
 *      ないときは-1を返す関数を作れ
 *
 * 解説:
 *      1次元配列を探索して
 *      目的の値があればその添え時（index）を
 *      なければ-1を返す関数となる
 *      int 位置 = f(int 探すデータ, int[] 表データ, int 表のサイズ)
 */
#include <stdio.h>
#define N 7

int linsearch(int x, int v[], int n) {
    int p = 0;
    while (p < n) {
        if (v[p] == x) break;
        p += 1;
    }
    if (p < n) return p;
    else return -1;
}

int main() {
    int a[N], i, t;
    for (i = 0; i < N; i++)
        scanf("%d", a+i);
    scanf("%d", &t);
    printf("%d \n", linsearch(t, a, N));
}

