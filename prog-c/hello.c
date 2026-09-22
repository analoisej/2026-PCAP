/*Comentario de Bloco
Programa: hello.c
Data: 2026.09.22
Autor: Ana Loise Jovino Prado
*/

// importa biblioteca padrão de entrada e saída
#include <stdio.h>

// defino a função principal do tipo int 
int main() {
    // printf == Saída --> Mostra na Tela; 
    //"entre aspas == texto"
    // comando se encerra com ; 
    printf("Hello, World!\n");
    // indica que chegou ao fim da função == retornando 0 
    
    // Recerber 2 valores sonar e mostrar o resultado 

    int num1=0, num2=0, soma=0;
    scanf("%d", &num1);
    scanf("%d", &num2);
    soma = num1 + num2;
    printf("X= %d\n", soma);
}

/*
para compilar == gcc <nome-do-arquivo> -o nome-do-programa 

para executar == ./nome-do-programa
*/