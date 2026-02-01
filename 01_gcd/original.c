/**
 * 問題:
 *      二つの正の整数の最大公約数（GCD）を求める
 *      ユークリッドのアルゴリズムをプログラムとして書け
 *
 * 解説:
 *      要は、以下のような関数を書けということ
 *      `int 最大公約数 = f(int 整数1, int 整数2)`
 */
#include <stdio.h>

int gcd(int m, int n) {
    int r, t;
    if (m < n) {
        t = m;
        m = n;
        n = t;
    }
    while (n != 0) {
        r = m % n;
        m = n;
        n = r;
    }
    return m;
}

int main() {
    int x, y;
    scanf("%d %d", &x, &y);
    printf("%d \n", gcd(x, y));
}
