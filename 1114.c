/*Comentario de Bloco
Programa: 1114.c
Data: 2026.10.08
Autor: Ana Loise Jovino Prado
*/
 #include <stdio.h>

 int main() {
    int senha;

    scanf("%d", &senha);

    while (senha != 2002) {

        printf("Senha Invalida\n");
        scanf("%d", &senha);
    }
    printf("Acesso Permitido\n");

    return 0;
 }