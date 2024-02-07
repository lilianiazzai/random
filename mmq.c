#include <stdio.h>
#define n 4

float calcular_a (float* ptr) {
    float a = 0;
    float numerador, denominador;

    numerador = (n * *(ptr + 2)) - (*(ptr) * *(ptr + 1));
    denominador = (n * *(ptr + 3)) - (*(ptr) * *(ptr));

    a = numerador / denominador;

    return a;
}

float calcular_b (float* ptr) {
    float b = 0;
    float numerador, denominador;

    numerador = (*(ptr) * *(ptr + 2)) - (*(ptr + 1) * *(ptr + 3));
    denominador = (*(ptr) * *(ptr)) - (n * *(ptr + 3));

    b = numerador / denominador;

    return b;
}

int main()
{
    float x[n], y[n], xy[n], xx[n];
    float somas[4] = {0, 0, 0, 0}; // guarda os valores dos somatorios de x, y, xy, e xx respectivamente

    printf("\n------------------------------------\n");
    printf("Valores de x e y: \n");

    for (int i = 0; i < n; i++) {
        printf("x%d : ", i);
        scanf("%f", &(x[i]));

        printf("y%d : ", i);
        scanf("%f", &(y[i]));

        xy[i] = x[i] * y[i];
        xx[i] = x[i] * x[i];

        // Fazendo os somatorios

        somas[0] += x[i];
        somas[1] += y[i];
        somas[2] += xy[i];
        somas[3] += xx[i];
    }
    printf("\n-----------------------------------------------------------\n");

    printf("x \t\t y \t\t xy \t\t x^2 \n");
    printf("-----------------------------------------------------------\n");
    for (int i = 0; i < n; i++) {
        printf("%f \t %f \t %f \t %f \n", x[i], y[i], xy[i], xx[i]);
    }
    printf("-----------------------------------------------------------\n");
    printf("%f \t %f \t %f \t %f \n", somas[0], somas[1], somas[2], somas[3]);
    
    
    printf("\ng(x) = %.3fx + (%.3f) \n", calcular_a(&(somas[0])), calcular_b(&(somas[0])));

    return 0;
}
