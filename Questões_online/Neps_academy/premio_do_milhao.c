/*Alice e Bia criaram uma página na Internet com informações sobre o Macaco-prego-de-peito-amarelo, uma espécie em extinção. A página mostra como todos podem ajudar a manter o habitat natural para evitar que a espécie seja extinta.

Uma empresa gostou tanto da iniciativa de Alice e Bia que prometeu doar um prêmio para que as duas amigas possam realizar outras iniciativas semelhantes. A empresa decidiu que o prêmio seria dado quando a soma do número de acessos à página chegasse a 1 milhão.

Dada a lista de acessos diários que ocorreram à página de Alice e Bia, escreva um programa para determinar quantos dias foram necessários para a soma dos acessos chegar a 1 milhão e as amigas ganharem o prêmio.*/
#include <stdio.h>

int main() {
    int dias;
    int soma = 0;
    int valor;
    int i; 
    int dias_definitivo = 0; 
    int conseguiu_1k = 0;
    scanf("%d", &dias);
    for (i = 1; i<=dias; i++) {
        scanf("%d", &valor);
        soma += valor;
        if (soma >= 1000000 && conseguiu_1k == 0){
            dias_definitivo = i;
            conseguiu_1k++;
        }
    }
    printf("%d", dias_definitivo);
    return 0;
    
}