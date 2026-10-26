#include <stdio.h>
#include <stdlib.h>
int main(void) {
    int vetor[10] = {0}, i, valor_desejado, quantidade_vetor[10] = {0}, x = 0, nao_desejado = 0;
    scanf("%d %d %d %d %d %d %d %d %d %d", &vetor[0],  &vetor[1],  &vetor[2],  &vetor[3], &vetor[4],  &vetor[5],  &vetor[6],  &vetor[7],  &vetor[8], &vetor[9]);
    scanf("%d", &valor_desejado);
    for (i = 0; i < 10; i++) {
        if (vetor[i] == valor_desejado) {
            quantidade_vetor[i] = vetor[i];
            x++;
        }
        else {
            nao_desejado++;
        }
    }
    
    if (x > 0) {
        printf("%d\n", x);
        for (i = 0; i< 10; i++) {
            if (quantidade_vetor[i] == vetor[i]) {
                printf("%d ", i);
            }
        }
    }
    else{
        printf("Mia x");
    }
    return 0;
}