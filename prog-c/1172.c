/*Comentario de Bloco
Programa: 1172.c
Data: 2026.10.06
Autor: Ana Loise Jovino Prado
*/

#include <stdio.h>

int main() {
    int x[10], i;

    for (i = 0; i < 10; i++) {
        scanf("%d", &x[i]);
        if (x[i] <= 0) {
            x[i] = 1;
        }
    }
    
    for (i = 0; i < 10; i++) {
        printf("X[%d] = %d\n", i, x[i]);
    }
    return 0;
}