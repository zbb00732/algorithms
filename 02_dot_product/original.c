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

