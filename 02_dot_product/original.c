/**
 * 問題:
 *      二つのベクトルを与えられて
 *      その内積の値を返す関数を作れ
 *
 * 解説:
 *      例として書かれたものは
 *      一つ目のベクトル、二つ目のベクトル、ベクトルの総数
 *      という3つの引数を受け取るものだった
 *      `double 内積 = f(double ベクトル1, double ベクトル2, int 総数)`
 */
#include <stdio.h>
double inprod(double x[], double y[], int n) {
    double s; int i;
    s = 0.0;
    for (i = 0; i < n; i++)
        s = s + x[i] * y[i];
    return s;
}

int main() {
    double a[3], b[3], inprod();
    int i;
    for (i = 0; i < 3; i++)
        scanf("%lf %lf", a+i, b+i);
    printf("%f \n", inprod(a, b, 3));
}

